from quart import Blueprint, render_template

nuevo_producto_bp = Blueprint('nuevo_producto', __name__)

@nuevo_producto_bp.route('/')
async def nuevo_producto():
    
    # Renderizar el HTML de pagos
    return await render_template('modal-nuevo-producto.html')