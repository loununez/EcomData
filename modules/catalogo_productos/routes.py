from quart import Blueprint, render_template, jsonify, request
from database.database import AsyncSessionLocal
from models.producto import Producto
from models.categoria import Categoria
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

catalogo_productos_bp = Blueprint('catalogo_productos', __name__)

@catalogo_productos_bp.route('/')
async def catalogo_productos():
    async with AsyncSessionLocal() as session:
        # Obtener todos los productos con sus categorías
        result = await session.execute(
            select(Producto)
            .options(selectinload(Producto.categoria))
        )
        productos_list = result.scalars().all()
        
        # Obtener todas las categorías para el dropdown
        categorias_result = await session.execute(select(Categoria))
        categorias_list = categorias_result.scalars().all()
    
    return await render_template('catalogo-productos.html', productos=productos_list, categorias=categorias_list)

@catalogo_productos_bp.route('/editar/<int:producto_id>', methods=['GET'])
async def obtener_producto(producto_id):
    """Obtener datos de un producto específico"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Producto)
            .where(Producto.id == producto_id)
            .options(selectinload(Producto.categoria))
        )
        producto = result.scalars().first()
        
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        
        return jsonify({
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "stock": producto.stock,
            "categoria_id": producto.categoria_id
        })

@catalogo_productos_bp.route('/actualizar/<int:producto_id>', methods=['POST'])
async def actualizar_producto(producto_id):
    """Actualizar datos de un producto"""
    try:
        data = await request.get_json()
        
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Producto).where(Producto.id == producto_id)
            )
            producto = result.scalars().first()
            
            if not producto:
                return jsonify({"error": "Producto no encontrado"}), 404
            
            # Actualizar campos
            producto.nombre = data.get('nombre', producto.nombre)
            producto.descripcion = data.get('descripcion', producto.descripcion)
            producto.precio = float(data.get('precio', producto.precio))
            producto.stock = int(data.get('stock', producto.stock))
            producto.categoria_id = data.get('categoria_id', producto.categoria_id)
            
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Producto actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@catalogo_productos_bp.route('/eliminar/<int:producto_id>', methods=['DELETE'])
async def eliminar_producto(producto_id):
    """Eliminar un producto"""
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Producto).where(Producto.id == producto_id)
            )
            producto = result.scalars().first()
            
            if not producto:
                return jsonify({"error": "Producto no encontrado"}), 404
            
            await session.delete(producto)
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Producto eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400