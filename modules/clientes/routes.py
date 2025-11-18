from quart import Blueprint, render_template, jsonify, request
from database.database import AsyncSessionLocal
from models.cliente import Cliente
from sqlalchemy.future import select

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/')
async def clientes():
    async with AsyncSessionLocal() as session:
        # Obtener todos los clientes
        result = await session.execute(select(Cliente))
        clientes_list = result.scalars().all()

    return await render_template('clientes.html', clientes=clientes_list)

@clientes_bp.route('/editar/<int:cliente_id>', methods=['GET'])
async def obtener_cliente(cliente_id):
    """Obtener datos de un cliente específico"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Cliente).where(Cliente.id == cliente_id)
        )
        cliente = result.scalars().first()
        
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404
        
        return jsonify({
            "id": cliente.id,
            "nombre": cliente.nombre,
            "email": cliente.email,
            "telefono": cliente.telefono,
            "direccion": cliente.direccion,
            "activo": cliente.activo
        })

@clientes_bp.route('/actualizar/<int:cliente_id>', methods=['POST'])
async def actualizar_cliente(cliente_id):
    """Actualizar datos de un cliente"""
    try:
        data = await request.get_json()
        
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Cliente).where(Cliente.id == cliente_id)
            )
            cliente = result.scalars().first()
            
            if not cliente:
                return jsonify({"error": "Cliente no encontrado"}), 404
            
            # Actualizar campos
            cliente.nombre = data.get('nombre', cliente.nombre)
            cliente.email = data.get('email', cliente.email)
            cliente.telefono = data.get('telefono', cliente.telefono)
            cliente.direccion = data.get('direccion', cliente.direccion)
            cliente.activo = data.get('activo', cliente.activo)
            
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Cliente actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@clientes_bp.route('/eliminar/<int:cliente_id>', methods=['DELETE'])
async def eliminar_cliente(cliente_id):
    """Eliminar un cliente"""
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Cliente).where(Cliente.id == cliente_id)
            )
            cliente = result.scalars().first()
            
            if not cliente:
                return jsonify({"error": "Cliente no encontrado"}), 404
            
            await session.delete(cliente)
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Cliente eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400