from quart import Blueprint, render_template, jsonify, request
from database.database import AsyncSessionLocal
from models.pago import Pago
from models.venta import Venta
from models.cliente import Cliente
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timedelta
from sqlalchemy import func

pagos_bp = Blueprint('pagos', __name__)

@pagos_bp.route('/')
async def pagos():
    async with AsyncSessionLocal() as session:
        # Obtener todos los pagos con relaciones
        result = await session.execute(
            select(Pago)
            .options(selectinload(Pago.venta).selectinload(Venta.cliente))
        )
        pagos_list = result.scalars().all()
        
        # Calcular indicadores
        hoy = datetime.utcnow().date()
        
        # Total de hoy
        result_total_hoy = await session.execute(
            select(func.sum(Pago.monto))
            .where(func.date(Pago.fecha_pago) == hoy)
        )
        total_hoy = result_total_hoy.scalar() or 0
        
        # Efectivo de hoy
        result_efectivo_hoy = await session.execute(
            select(func.sum(Pago.monto))
            .where(func.date(Pago.fecha_pago) == hoy)
            .where(Pago.metodo == 'Efectivo')
        )
        efectivo_hoy = result_efectivo_hoy.scalar() or 0
        
        # Total pagos en efectivo (historial)
        result_total_efectivo = await session.execute(
            select(func.sum(Pago.monto))
            .where(Pago.metodo == 'Efectivo')
        )
        total_efectivo = result_total_efectivo.scalar() or 0
        
        # Tarjetas de hoy
        result_tarjetas_hoy = await session.execute(
            select(func.sum(Pago.monto))
            .where(func.date(Pago.fecha_pago) == hoy)
            .where(Pago.metodo == 'Tarjeta')
        )
        tarjetas_hoy = result_tarjetas_hoy.scalar() or 0
        
        indicadores = {
            'total_hoy': float(total_hoy),
            'efectivo_hoy': float(efectivo_hoy),
            'total_efectivo': float(total_efectivo),
            'tarjetas_hoy': float(tarjetas_hoy)
        }

    return await render_template('pagos.html', pagos=pagos_list, indicadores=indicadores)

@pagos_bp.route('/editar/<int:pago_id>', methods=['GET'])
async def obtener_pago(pago_id):
    """Obtener datos de un pago específico"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Pago)
            .where(Pago.id == pago_id)
            .options(selectinload(Pago.venta))
        )
        pago = result.scalars().first()
        
        if not pago:
            return jsonify({"error": "Pago no encontrado"}), 404
        
        return jsonify({
            "id": pago.id,
            "venta_id": pago.venta_id,
            "monto": pago.monto,
            "metodo": pago.metodo,
            "fecha_pago": pago.fecha_pago.isoformat() if pago.fecha_pago else None
        })

@pagos_bp.route('/actualizar/<int:pago_id>', methods=['POST'])
async def actualizar_pago(pago_id):
    """Actualizar datos de un pago"""
    try:
        data = await request.get_json()
        
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Pago).where(Pago.id == pago_id)
            )
            pago = result.scalars().first()
            
            if not pago:
                return jsonify({"error": "Pago no encontrado"}), 404
            
            # Actualizar campos
            pago.monto = float(data.get('monto', pago.monto))
            pago.metodo = data.get('metodo', pago.metodo)
            
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Pago actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pagos_bp.route('/eliminar/<int:pago_id>', methods=['DELETE'])
async def eliminar_pago(pago_id):
    """Eliminar un pago"""
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(Pago).where(Pago.id == pago_id)
            )
            pago = result.scalars().first()
            
            if not pago:
                return jsonify({"error": "Pago no encontrado"}), 404
            
            await session.delete(pago)
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Pago eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400