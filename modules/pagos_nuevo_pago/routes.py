from quart import Blueprint, render_template, jsonify, request
from database.database import AsyncSessionLocal
from models.pago import Pago
from models.venta import Venta
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from datetime import datetime

pagos_nuevo_pago_bp = Blueprint('pagos_nuevo_pago', __name__)

@pagos_nuevo_pago_bp.route('/')
async def pagos_nuevo_pago():
    async with AsyncSessionLocal() as session:
        # Obtener todas las ventas sin pago o con pagos pendientes
        result = await session.execute(
            select(Venta)
            .options(selectinload(Venta.cliente))
        )
        ventas_list = result.scalars().all()
    
    return await render_template('pagos-nuevo-pago.html', ventas=ventas_list)

@pagos_nuevo_pago_bp.route('/crear', methods=['POST'])
async def crear_pago():
    """Crear un nuevo pago"""
    try:
        data = await request.get_json()
        
        async with AsyncSessionLocal() as session:
            # Verificar que la venta exista
            result = await session.execute(
                select(Venta).where(Venta.id == data.get('venta_id'))
            )
            venta = result.scalars().first()
            
            if not venta:
                return jsonify({"error": "Venta no encontrada"}), 404
            
            # Crear el pago
            nuevo_pago = Pago(
                venta_id=data.get('venta_id'),
                monto=float(data.get('monto')),
                metodo=data.get('metodo', 'Efectivo'),
                fecha_pago=datetime.utcnow()
            )
            
            session.add(nuevo_pago)
            await session.commit()
            
        return jsonify({"success": True, "mensaje": "Pago creado correctamente", "pago_id": nuevo_pago.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pagos_nuevo_pago_bp.route('/ventas', methods=['GET'])
async def obtener_ventas():
    """Obtener lista de ventas para el formulario"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Venta)
            .options(selectinload(Venta.cliente))
        )
        ventas_list = result.scalars().all()
        
        ventas_data = [
            {
                "id": venta.id,
                "numero": f"VTA-{venta.id:03d}",
                "cliente": venta.cliente.nombre if venta.cliente else "Cliente General",
                "total": venta.total
            }
            for venta in ventas_list
        ]
        
    return jsonify(ventas_data)