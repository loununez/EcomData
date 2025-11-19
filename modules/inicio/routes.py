from quart import Blueprint, render_template

inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route('/')
async def inicio():
    
    # Renderizar el HTML del index
    return await render_template('index.html')