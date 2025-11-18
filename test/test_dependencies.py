"""
Script para verificar que todas las dependencias requeridas estén instaladas.
Comprueba que los módulos principales de la aplicación se importen correctamente.
"""

import sys
import os
import importlib
from typing import List, Tuple

# Configurar encoding UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Agregar la carpeta padre al path para poder importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


DEPENDENCIAS_REQUERIDAS = [
    ('quart', 'Quart'),
    ('sqlalchemy', 'SQLAlchemy'),
    ('werkzeug', 'Werkzeug'),
    ('jinja2', 'Jinja2'),
    ('aiosqlite', 'aiosqlite'),
]

MODULOS_INTERNOS = [
    'database.database',
    'models.usuario',
    'models.rol',
    'models.producto',
    'models.categoria',
    'models.cliente',
    'models.pago',
    'models.venta',
    'models.detalle_venta',
    'models.inventario',
    'models.configuracion',
]


def verificar_dependencias():
    """Verifica que todas las dependencias externas estén disponibles"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE DEPENDENCIAS EXTERNAS")
    print("="*70 + "\n")
    
    resultados = {'exitosas': 0, 'faltantes': []}
    
    for nombre_paquete, nombre_mostrar in DEPENDENCIAS_REQUERIDAS:
        try:
            importlib.import_module(nombre_paquete)
            print(f"✓ {nombre_mostrar}: Instalado")
            resultados['exitosas'] += 1
        except ImportError:
            print(f"✗ {nombre_mostrar}: NO ENCONTRADO")
            resultados['faltantes'].append(nombre_paquete)
    
    print("\n" + "="*70)
    return resultados


def verificar_modulos_internos():
    """Verifica que todos los módulos internos importe sin errores"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE MÓDULOS INTERNOS")
    print("="*70 + "\n")
    
    resultados = {'exitosos': 0, 'errores': []}
    
    for modulo in MODULOS_INTERNOS:
        try:
            importlib.import_module(modulo)
            print(f"✓ {modulo}: Importado correctamente")
            resultados['exitosos'] += 1
        except Exception as e:
            print(f"✗ {modulo}: Error - {str(e)[:50]}")
            resultados['errores'].append((modulo, str(e)))
    
    print("\n" + "="*70)
    return resultados


def main():
    """Ejecuta todas las verificaciones"""
    print("\n" + "="*70)
    print("ANÁLISIS DE DEPENDENCIAS Y MÓDULOS")
    print("="*70)
    
    deps = verificar_dependencias()
    mods = verificar_modulos_internos()
    
    print("\n" + "="*70)
    print("RESUMEN")
    print("="*70)
    print(f"Dependencias externas: {deps['exitosas']} OK, {len(deps['faltantes'])} faltantes")
    print(f"Módulos internos: {mods['exitosos']} OK, {len(mods['errores'])} errores")
    print("="*70 + "\n")
    
    total_errores = len(deps['faltantes']) + len(mods['errores'])
    return total_errores == 0


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
