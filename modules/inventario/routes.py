from quart import Blueprint, render_template

inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/')
async def inventario():
    
    # Renderizar el HTML de inventario
    return await render_template('inventario.html')