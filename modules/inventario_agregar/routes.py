from quart import Blueprint, render_template

inventario_agregar_bp = Blueprint('inventario_agregar', __name__)

@inventario_agregar_bp.route('/')
async def inventario_agregar():
    
    # Renderizar el HTML de inventario_agregar
    return await render_template('inventario-agregar-producto.html')