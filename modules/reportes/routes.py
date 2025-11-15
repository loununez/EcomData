from quart import Blueprint, render_template

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/')
async def reportes():
    
    # Renderizar el HTML de pagos
    return await render_template('reportes.html')