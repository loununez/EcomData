from quart import Blueprint, render_template

administracion_bp = Blueprint('administracion', __name__)

@administracion_bp.route('/')
async def administracion():
    
    # Renderizar el HTML de administracion
    return await render_template('administracion.html')