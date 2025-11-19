# routes/rol_routes.py
from quart import Blueprint, jsonify, request
from database.database import get_db
from models.rol import Rol

rol_bp = Blueprint("rol_bp", __name__)

# Listar todos los roles
@rol_bp.route("/", methods=["GET"])
async def listar_roles():
    async for db in get_db():
        roles = db.query(Rol).all()
        return jsonify([{"id": r.id, "nombre": r.nombre, "descripcion": r.descripcion} for r in roles])


# Obtener un rol por ID
@rol_bp.route("/<int:rol_id>", methods=["GET"])
async def obtener_rol(rol_id: int):
    async for db in get_db():
        rol = db.query(Rol).filter(Rol.id == rol_id).first()
        if not rol:
            return jsonify({"error": "Rol no encontrado"}), 404
        return jsonify({"id": rol.id, "nombre": rol.nombre, "descripcion": rol.descripcion})


# Crear un nuevo rol
@rol_bp.route("/", methods=["POST"])
async def crear_rol():
    data = await request.get_json()
    nombre = data.get("nombre")
    descripcion = data.get("descripcion", "")

    async for db in get_db():
        rol_existente = db.query(Rol).filter(Rol.nombre == nombre).first()
        if rol_existente:
            return jsonify({"error": "El rol ya existe"}), 400

        nuevo_rol = Rol(nombre=nombre, descripcion=descripcion)
        db.add(nuevo_rol)
        db.commit()
        db.refresh(nuevo_rol)

        return jsonify({"mensaje": "Rol creado correctamente", "rol_id": nuevo_rol.id})


# Actualizar un rol
@rol_bp.route("/<int:rol_id>", methods=["PUT"])
async def actualizar_rol(rol_id: int):
    data = await request.get_json()
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")

    async for db in get_db():
        rol = db.query(Rol).filter(Rol.id == rol_id).first()
        if not rol:
            return jsonify({"error": "Rol no encontrado"}), 404

        if nombre:
            rol.nombre = nombre
        if descripcion:
            rol.descripcion = descripcion

        db.commit()
        db.refresh(rol)
        return jsonify({"mensaje": "Rol actualizado correctamente", "rol_id": rol.id})


# Eliminar un rol
@rol_bp.route("/<int:rol_id>", methods=["DELETE"])
async def eliminar_rol(rol_id: int):
    async for db in get_db():
        rol = db.query(Rol).filter(Rol.id == rol_id).first()
        if not rol:
            return jsonify({"error": "Rol no encontrado"}), 404

        db.delete(rol)
        db.commit()
        return jsonify({"mensaje": "Rol eliminado correctamente"})
