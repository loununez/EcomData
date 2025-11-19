from quart import Blueprint, render_template

analisis_negocio_productos_bp = Blueprint('analisis_negocio_productos', __name__)

@analisis_negocio_productos_bp.route('/')
async def analisis_negocio_productos():
    
    # Renderizar el HTML de analisis negocio productos
    return await render_template('analisis-negocio-producto.html')