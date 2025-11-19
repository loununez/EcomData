# modules/usuarios/routes.py
from quart import Blueprint, render_template, jsonify, request
from database.database import AsyncSessionLocal
from models.usuario import Usuario
from models.rol import Rol
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from werkzeug.security import generate_password_hash

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
async def usuarios():
    async with AsyncSessionLocal() as session:
        # Obtener todos los usuarios con sus roles
        result = await session.execute(
            select(Usuario)
            .options(selectinload(Usuario.rol))
        )
        usuarios_list = result.scalars().all()
        
        # Obtener todos los roles para el dropdown
        roles_result = await session.execute(select(Rol))
        roles_list = roles_result.scalars().all()

    return await render_template('usuario.html', usuarios=usuarios_list, roles=roles_list)

@usuarios_bp.route('/editar/<int:usuario_id>', methods=['GET'])
async def obtener_usuario(usuario_id):
    """Obtener datos de un usuario específico"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Usuario)
            .where(Usuario.id == usuario_id)
            .options(selectinload(Usuario.rol))
        )
        usuario = result.scalars().first()
        
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404
        
        return jsonify({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol_id": usuario.rol_id,
            "activo": usuario.activo
        })

@usuarios_bp.route('/actualizar/<int:usuario_id>', methods=['POST'])
async def actualizar_usuario(usuario_id):
    """Actualizar datos de un usuario"""
    try:
        data = await request.get_json()
        
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Usuario).where(Usuario.id == usuario_id)
            )
            usuario = result.scalars().first()
            
            if not usuario:
                return jsonify({"error": "Usuario no encontrado"}), 404
            
            # Actualizar campos
            usuario.nombre = data.get('nombre', usuario.nombre)
            usuario.email = data.get('email', usuario.email)
            usuario.rol_id = data.get('rol_id', usuario.rol_id)
            usuario.activo = data.get('activo', usuario.activo)
            
            # Si se proporciona una nueva contraseña
            if data.get('password') and data.get('password').strip():
                usuario.password = generate_password_hash(data.get('password'))
            
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Usuario actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuarios_bp.route('/eliminar/<int:usuario_id>', methods=['DELETE'])
async def eliminar_usuario(usuario_id):
    """Eliminar un usuario"""
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Usuario).where(Usuario.id == usuario_id)
            )
            usuario = result.scalars().first()
            
            if not usuario:
                return jsonify({"error": "Usuario no encontrado"}), 404
            
            await session.delete(usuario)
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Usuario eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400