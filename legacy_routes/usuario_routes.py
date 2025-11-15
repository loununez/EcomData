# routes/usuario_routes.py
from quart import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from database.database import get_db
from models.usuario import Usuario
from models.rol import Rol
import bcrypt

usuario_bp = Blueprint('usuario_bp', __name__)

# Obtener todos los usuarios
@usuario_bp.route("/", methods=["GET"])
async def obtener_usuarios():
    async for db in get_db():
        usuarios = db.query(Usuario).all()
        return jsonify([
            {
                "id": u.id,
                "nombre": u.nombre,
                "email": u.email,
                "rol_id": u.rol_id
            }
            for u in usuarios
        ])


# Obtener un usuario por ID
@usuario_bp.route("/<int:usuario_id>", methods=["GET"])
async def obtener_usuario(usuario_id: int):
    async for db in get_db():
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return jsonify({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol_id": usuario.rol_id
        })


# Crear un nuevo usuario
@usuario_bp.route("/", methods=["POST"])
async def crear_usuario():
    data = await request.get_json()
    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")
    rol_nombre = data.get("rol_nombre")

    async for db in get_db():
        # Verificar si ya existe el email
        usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
        if usuario_existente:
            return jsonify({"error": "El email ya está registrado"}), 400

        # Buscar rol
        rol = db.query(Rol).filter(Rol.nombre == rol_nombre).first()
        if not rol:
            return jsonify({"error": "Rol no encontrado"}), 404

        # Hashear contraseña
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            password=hashed_pw,
            rol_id=rol.id
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        return jsonify({
            "mensaje": "Usuario creado correctamente",
            "usuario_id": nuevo_usuario.id
        })


# Actualizar un usuario
@usuario_bp.route("/<int:usuario_id>", methods=["PUT"])
async def actualizar_usuario(usuario_id: int):
    data = await request.get_json()
    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")
    rol_nombre = data.get("rol_nombre")

    async for db in get_db():
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        if nombre:
            usuario.nombre = nombre
        if email:
            usuario.email = email
        if password:
            usuario.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        if rol_nombre:
            rol = db.query(Rol).filter(Rol.nombre == rol_nombre).first()
            if not rol:
                return jsonify({"error": "Rol no encontrado"}), 404
            usuario.rol_id = rol.id

        db.commit()
        db.refresh(usuario)

        return jsonify({
            "mensaje": "Usuario actualizado correctamente",
            "usuario_id": usuario.id
        })


# Eliminar un usuario
@usuario_bp.route("/<int:usuario_id>", methods=["DELETE"])
async def eliminar_usuario(usuario_id: int):
    async for db in get_db():
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.delete(usuario)
        db.commit()
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
