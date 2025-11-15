from quart import Blueprint, render_template

pagos_bp = Blueprint('pagos', __name__)

@pagos_bp.route('/')
async def pagos():
    
    # Renderizar el HTML de pagos
    return await render_template('pagos.html')