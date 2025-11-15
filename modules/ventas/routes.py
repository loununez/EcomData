from quart import Blueprint, render_template

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.route('/')
async def ventas():
    
    # Renderizar el HTML de ventas
    return await render_template('ventas.html')