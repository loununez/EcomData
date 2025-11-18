import asyncio
import argparse
from database.database import engine, Base
from database.database import Base

# Importar todos los modelos ANTES de crear las tablas
from models.rol import Rol
from models.usuario import Usuario
from models.categoria import Categoria
from models.producto import Producto
from models.inventario import Inventario
from models.venta import Venta
from models.pago import Pago
from models.configuracion import ConfiguracionGeneral, ConfiguracionSeguridad, ConfiguracionNotificacion


async def init_db(reset: bool = False):
    """Inicializa la base de datos.

    Por defecto solo crea las tablas que no existen. Si se pasa `--reset`,
    se borran todas las tablas antes de crearlas (uso en entornos de desarrollo).
    """
    async with engine.begin() as conn:
        if reset:
            await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    print("Base de datos SQLite inicializada correctamente")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inicializar base de datos SQLite")
    parser.add_argument('--reset', action='store_true', help='Borrar todas las tablas antes de crear (desarrollo)')
    args = parser.parse_args()

    asyncio.run(init_db(reset=args.reset))