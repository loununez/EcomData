from quart import Blueprint, render_template

analisis_negocio_resumen_bp = Blueprint('analisis_negocio_resumen', __name__)

@analisis_negocio_resumen_bp.route('/')
async def analisis_negocio_resumen():
    
    # Renderizar el HTML de analisis negocio resumen
    return await render_template('analisis-negocio-resumen.html')