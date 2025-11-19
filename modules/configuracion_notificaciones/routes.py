from quart import Blueprint, render_template

configuracion_notificaciones_bp = Blueprint('configuracion_notificaciones', __name__)

@configuracion_notificaciones_bp.route('/')
async def configuracion_notificaciones():
    
    # Renderizar el HTML de pagos
    return await render_template('configuracion_notificaciones.html')