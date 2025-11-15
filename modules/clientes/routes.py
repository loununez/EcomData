from quart import Blueprint, render_template

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/')
async def  clientes():
    
    # Renderizar el HTML de clientes
    return await render_template('clientes.html')