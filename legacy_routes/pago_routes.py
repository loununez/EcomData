from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.pago import Pago
from models.venta import Venta
from datetime import datetime

pago_bp = Blueprint('pago_bp', __name__, template_folder='../templates')


# Listado de pagos
@pago_bp.route('/', methods=['GET'])
async def listado_pagos():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Pago))
        pagos = result.scalars().all()
    return await render_template('listado-pagos.html', pagos=pagos)


# Crear nuevo pago (desde formulario)
@pago_bp.route('/nuevo', methods=['GET', 'POST'])
async def nuevo_pago():
    async with AsyncSessionLocal() as session:
        if request.method == 'GET':
            # traer ventas para seleccionar
            ventas_result = await session.execute(select(Venta))
            ventas = ventas_result.scalars().all()
            return await render_template('modal-nuevo-pago.html', ventas=ventas)

        # POST: procesar formulario
        form = await request.form
        venta_id = int(form.get('venta_id'))
        metodo_pago = form.get('metodo_pago')
        monto = float(form.get('monto'))

        venta = await session.get(Venta, venta_id)
        if not venta:
            return jsonify({"error": "Venta no encontrada"}), 404

        # Validar si la venta ya tiene pago
        result = await session.execute(select(Pago).where(Pago.venta_id == venta_id))
        pago_existente = result.scalar_one_or_none()
        if pago_existente:
            return jsonify({"error": "La venta ya tiene un pago registrado"}), 400

        nuevo_pago = Pago(
            venta_id=venta_id,
            metodo_pago=metodo_pago,
            monto=monto,
            fecha_pago=datetime.utcnow()
        )
        session.add(nuevo_pago)
        await session.commit()

    return redirect(url_for('pago_bp.listado_pagos'))


# Eliminar pago
@pago_bp.route('/<int:pago_id>/eliminar', methods=['POST'])
async def eliminar_pago(pago_id: int):
    async with AsyncSessionLocal() as session:
        pago = await session.get(Pago, pago_id)
        if not pago:
            return jsonify({"error": "Pago no encontrado"}), 404

        await session.delete(pago)
        await session.commit()

    return redirect(url_for('pago_bp.listado_pagos'))
