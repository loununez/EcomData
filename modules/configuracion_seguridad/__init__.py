"""Blueprint para módulo de configuración de seguridad."""

from quart import Blueprint

configuracion_seguridad_bp = Blueprint(
    'configuracion_seguridad',
    __name__,
    url_prefix='/configuracion_seguridad'
)
