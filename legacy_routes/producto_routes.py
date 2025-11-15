from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.producto import Producto
from models.categoria import Categoria
from datetime import datetime

producto_bp = Blueprint('producto_bp', __name__, template_folder='../templates')


# Listado de productos
@producto_bp.route('/', methods=['GET'])
async def listado_productos():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Producto))
        productos = result.scalars().all()
    return await render_template('catalogo-productos.html', productos=productos)


# Formulario para crear nuevo producto
@producto_bp.route('/nuevo', methods=['GET'])
async def formulario_nuevo_producto():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Categoria))
        categorias = result.scalars().all()
    return await render_template('modal-nuevo-producto.html', categorias=categorias)


# Guardar nuevo producto
@producto_bp.route('/guardar', methods=['POST'])
async def guardar_producto():
    form = await request.form
    nombre = form.get('nombreProducto') or form.get('nombre')
    sku = form.get('sku')
    categoria_id = form.get('categoria')
    costo = form.get('costo') or 0
    precio = form.get('precio') or 0
    stock_inicial = form.get('stockInicial') or 0
    stock_minimo = form.get('stockMinimo') or 0
    descripcion = form.get('descripcionProducto') or ''

    async with AsyncSessionLocal() as session:
        categoria_obj = None
        if categoria_id:
            try:
                categoria_id_int = int(categoria_id)
                result = await session.execute(select(Categoria).where(Categoria.id == categoria_id_int))
                categoria_obj = result.scalar_one_or_none()
            except (ValueError, TypeError):
                result = await session.execute(select(Categoria).where(Categoria.nombre == categoria_id))
                categoria_obj = result.scalar_one_or_none()

        nuevo = Producto(
            nombre=nombre,
            sku=sku,
            categoria_id=categoria_obj.id if categoria_obj else None,
            costo=float(costo) if costo != '' else 0.0,
            precio=float(precio) if precio != '' else 0.0,
            stock_inicial=int(stock_inicial),
            stock_minimo=int(stock_minimo),
            descripcion=descripcion,
            fecha_creacion=datetime.utcnow()
        )

        session.add(nuevo)
        await session.commit()

    return redirect(url_for('producto_bp.listado_productos'))


# Eliminar un producto
@producto_bp.route('/<int:producto_id>/eliminar', methods=['POST'])
async def eliminar_producto(producto_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Producto).where(Producto.id == producto_id))
        producto = result.scalar_one_or_none()
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        await session.delete(producto)
        await session.commit()
    return redirect(url_for('producto_bp.listado_productos'))
