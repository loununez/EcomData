from quart import Blueprint, render_template

configuracion_general_bp = Blueprint('configuracion_general', __name__)

@configuracion_general_bp.route('/')
async def configuracion_general():
    
    # Renderizar el HTML de pagos
    return await render_template('configuracion_general.html')