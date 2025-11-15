from quart import Blueprint, render_template

pagos_nuevo_pago_bp = Blueprint('pagos_nuevo_pago', __name__)

@pagos_nuevo_pago_bp.route('/')
async def  pagos_nuevo_pago():
    
    # Renderizar el HTML de pagos nuevo pagos
    return await render_template('pagos-nuevo-pago.html')