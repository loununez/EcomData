from quart import Blueprint, render_template

analisis_negocio_clientes_bp = Blueprint('analisis_negocio_clientes', __name__)

@analisis_negocio_clientes_bp.route('/')
async def analisis_negocio_clientes():
    
    # Renderizar el HTML de analisis negocio clientes
    return await render_template('analisis-negocio-cliente.html')