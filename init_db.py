"""
Script para inicializar la base de datos.
Debe ejecutarse desde la carpeta raíz del proyecto.
"""

import asyncio
import sys
import os

# Agregar carpeta actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.database import engine, Base

# Importar todos los modelos ANTES de crear las tablas
from models.rol import Rol
from models.usuario import Usuario
from models.categoria import Categoria
from models.producto import Producto
from models.inventario import Inventario
from models.venta import Venta
from models.detalle_venta import DetalleVenta
from models.pago import Pago
from models.configuracion import ConfiguracionGeneral, ConfiguracionSeguridad, ConfiguracionNotificacion


async def init_db(reset=False):
    """Inicializa la base de datos."""
    try:
        async with engine.begin() as conn:
            if reset:
                print("Eliminando todas las tablas...")
                await conn.run_sync(Base.metadata.drop_all)
            print("Creando tablas...")
            await conn.run_sync(Base.metadata.create_all)
        
        print("✓ Base de datos inicializada correctamente")
        return True
    except Exception as e:
        print(f"✗ Error al inicializar la base de datos: {e}")
        return False


def main():
    """Función principal"""
    reset = '--reset' in sys.argv
    
    if reset:
        confirmacion = input("¿Desea reinicializar la base de datos? (s/n): ")
        if confirmacion.lower() != 's':
            print("Operación cancelada")
            return False
    
    return asyncio.run(init_db(reset))


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
