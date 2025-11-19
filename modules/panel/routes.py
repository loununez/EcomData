from quart import Blueprint, render_template

panel_bp = Blueprint('panel', __name__)

@panel_bp.route('/')
async def panel():
    
    # Renderizar el HTML del panel
    return await render_template('panel.html')