from quart import Blueprint, render_template

ventas_carrito_bp = Blueprint('ventas_carrito', __name__)

@ventas_carrito_bp.route('/')
async def ventas_carrito():
    
    # Renderizar el HTML de ventas_carrito
    return await render_template('ventas-carrito.html')