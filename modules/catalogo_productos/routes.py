from quart import Blueprint, render_template

catalogo_productos_bp = Blueprint('catalogo_productos', __name__)

@catalogo_productos_bp.route('/')
async def catalogo_productos():
    
    # Renderizar el HTML de administracion
    return await render_template('catalogo-productos.html')