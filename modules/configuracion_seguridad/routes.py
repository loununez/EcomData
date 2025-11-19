"""
Rutas para configuración de seguridad.
Gestiona políticas de contraseña, doble factor, etc.
"""

from quart import render_template
from . import configuracion_seguridad_bp


@configuracion_seguridad_bp.route('/')
async def index():
    """Página principal de configuración de seguridad"""
    return await render_template('configuracion_seguridad.html')
