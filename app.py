# app.py

# Importo los módulos
from quart import Quart, render_template
import os
from modules.inicio.routes import inicio_bp
from modules.panel.routes import panel_bp
from modules.ventas.routes import ventas_bp
from modules.ventas_carrito.routes import ventas_carrito_bp
from modules.inventario.routes import inventario_bp
from modules.inventario_agregar.routes import inventario_agregar_bp
from modules.analisis_negocio_resumen.routes import analisis_negocio_resumen_bp
from modules.analisis_negocio_clientes.routes import analisis_negocio_clientes_bp
from modules.analisis_negocio_productos.routes import analisis_negocio_productos_bp
from modules.clientes.routes import clientes_bp
from modules.pagos.routes import pagos_bp
from modules.pagos_nuevo_pago.routes import pagos_nuevo_pago_bp
from modules.administracion.routes import administracion_bp
from modules.usuarios.routes import usuarios_bp
from modules.usuarios_agregar.routes import usuarios_agregar_bp
from modules.catalogo_productos.routes import catalogo_productos_bp
from modules.catalogo_categorias.routes import catalogo_categorias_bp
from modules.nuevo_producto.routes import nuevo_producto_bp
from modules.nueva_categoria.routes import nueva_categoria_bp
from modules.reportes.routes import reportes_bp
from modules.configuracion_general.routes import configuracion_general_bp
from modules.configuracion_notificaciones.routes import configuracion_notificaciones_bp
from modules.auth.routes import auth_bp

def create_app():
    app = Quart(__name__, template_folder='templates')

    # Registro los blueprints
    app.register_blueprint(inicio_bp, url_prefix='/inicio')
    app.register_blueprint(panel_bp, url_prefix='/panel')
    app.register_blueprint(ventas_bp, url_prefix='/ventas')
    app.register_blueprint(ventas_carrito_bp, url_prefix='/ventas_carrito')
    app.register_blueprint(inventario_bp, url_prefix='/inventario')
    app.register_blueprint(inventario_agregar_bp, url_prefix='/inventario_agregar')
    app.register_blueprint(analisis_negocio_resumen_bp, url_prefix='/analisis_negocio_resumen')
    app.register_blueprint(analisis_negocio_clientes_bp, url_prefix='/analisis_negocio_clientes')
    app.register_blueprint(analisis_negocio_productos_bp, url_prefix='/analisis_negocio_productos')
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(pagos_bp, url_prefix='/pagos')
    app.register_blueprint(pagos_nuevo_pago_bp, url_prefix='/pagos_nuevo_pago')
    app.register_blueprint(administracion_bp, url_prefix='/administracion')
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(usuarios_agregar_bp, url_prefix='/usuarios_agregar')
    app.register_blueprint(catalogo_productos_bp, url_prefix='/catalogo_productos')
    app.register_blueprint(catalogo_categorias_bp, url_prefix='/catalogo_categorias')
    app.register_blueprint(nuevo_producto_bp, url_prefix='/nuevo_producto')
    app.register_blueprint(nueva_categoria_bp, url_prefix='/nueva_categoria')
    app.register_blueprint(reportes_bp, url_prefix='/reportes')
    app.register_blueprint(configuracion_general_bp, url_prefix='/configuracion_general')
    app.register_blueprint(configuracion_notificaciones_bp, url_prefix='/configuracion_notificaciones')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Set secret key for session handling (read from env or use dev fallback)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

    # Ruta raíz: renderiza la página principal o redirige al blueprint de inicio
    @app.route('/')
    async def index():
        return await render_template('index.html')

    return app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)