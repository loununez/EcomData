from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.venta import Venta
from models.cliente import Cliente
from models.producto import Producto
from models.pago import Pago
from datetime import datetime

venta_bp = Blueprint('venta_bp', __name__, template_folder='../templates')


# Listado de ventas
@venta_bp.route('/', methods=['GET'])
async def listado_ventas():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Venta))
        ventas = result.scalars().all()
    return await render_template('listado-ventas.html', ventas=ventas)


# Crear nueva venta (desde formulario)
@venta_bp.route('/nuevo', methods=['GET', 'POST'])
async def nueva_venta():
    async with AsyncSessionLocal() as session:
        if request.method == 'GET':
            # traer clientes y productos para el formulario
            clientes_result = await session.execute(select(Cliente))
            productos_result = await session.execute(select(Producto))
            clientes = clientes_result.scalars().all()
            productos = productos_result.scalars().all()
            return await render_template('modal-nueva-venta.html', clientes=clientes, productos=productos)

        # POST: procesar formulario
        form = await request.form
        cliente_id = int(form.get('cliente_id'))
        producto_id = int(form.get('producto_id'))
        cantidad = int(form.get('cantidad'))
        metodo_pago = form.get('metodo_pago')

        cliente = await session.get(Cliente, cliente_id)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404

        producto = await session.get(Producto, producto_id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        if producto.stock < cantidad:
            return jsonify({"error": "Stock insuficiente"}), 400

        total = producto.precio * cantidad

        nueva_venta = Venta(
            cliente_id=cliente.id,
            producto_id=producto.id,
            cantidad=cantidad,
            total=total,
            fecha=datetime.utcnow()
        )
        session.add(nueva_venta)
        producto.stock -= cantidad

        pago = Pago(
            venta=nueva_venta,
            metodo_pago=metodo_pago,
            monto=total,
            fecha_pago=datetime.utcnow()
        )
        session.add(pago)

        await session.commit()

    return redirect(url_for('venta_bp.listado_ventas'))


# Eliminar venta
@venta_bp.route('/<int:venta_id>/eliminar', methods=['POST'])
async def eliminar_venta(venta_id: int):
    async with AsyncSessionLocal() as session:
        venta = await session.get(Venta, venta_id)
        if not venta:
            return jsonify({"error": "Venta no encontrada"}), 404

        producto = await session.get(Producto, venta.producto_id)
        if producto:
            producto.stock += venta.cantidad

        pago_result = await session.execute(select(Pago).where(Pago.venta_id == venta.id))
        pago = pago_result.scalar_one_or_none()
        if pago:
            await session.delete(pago)

        await session.delete(venta)
        await session.commit()

    return redirect(url_for('venta_bp.listado_ventas'))
