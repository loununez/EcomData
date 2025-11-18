"""
Script de prueba para verificar la integridad de los modelos de datos.
Valida que todos los modelos carguen correctamente y tengan los atributos esperados.
"""

import sys
import os

# Configurar encoding UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.usuario import Usuario
from models.rol import Rol
from models.producto import Producto
from models.categoria import Categoria
from models.cliente import Cliente
from models.pago import Pago
from models.venta import Venta
from models.detalle_venta import DetalleVenta
from models.inventario import Inventario
from models.configuracion import ConfiguracionGeneral, ConfiguracionNotificacion, ConfiguracionSeguridad


def test_modelos():
    """Prueba que todos los modelos carguen correctamente"""
    print("\n" + "="*70)
    print("PRUEBA DE INTEGRIDAD DE MODELOS")
    print("="*70 + "\n")
    
    modelos = [
        ('Usuario', Usuario),
        ('Rol', Rol),
        ('Producto', Producto),
        ('Categoria', Categoria),
        ('Cliente', Cliente),
        ('Pago', Pago),
        ('Venta', Venta),
        ('DetalleVenta', DetalleVenta),
        ('Inventario', Inventario),
        ('ConfiguracionGeneral', ConfiguracionGeneral),
        ('ConfiguracionNotificacion', ConfiguracionNotificacion),
        ('ConfiguracionSeguridad', ConfiguracionSeguridad),
    ]
    
    resultados = {
        'exitosos': 0,
        'errores': 0,
        'detalles': []
    }
    
    for nombre_modelo, clase_modelo in modelos:
        try:
            # Verificar que la clase tenga la tabla definida
            if hasattr(clase_modelo, '__tablename__'):
                atributos = [attr for attr in dir(clase_modelo) if not attr.startswith('_')]
                resultados['exitosos'] += 1
                detalles = f"✓ {nombre_modelo}: Cargado correctamente ({len(atributos)} atributos)"
                print(detalles)
                resultados['detalles'].append(detalles)
            else:
                resultados['errores'] += 1
                detalles = f"✗ {nombre_modelo}: No tiene __tablename__ definido"
                print(detalles)
                resultados['detalles'].append(detalles)
        except Exception as e:
            resultados['errores'] += 1
            detalles = f"✗ {nombre_modelo}: Error - {str(e)}"
            print(detalles)
            resultados['detalles'].append(detalles)
    
    print("\n" + "="*70)
    print(f"Resultados: {resultados['exitosos']} exitosos, {resultados['errores']} errores")
    print("="*70 + "\n")
    
    return resultados


if __name__ == '__main__':
    resultados = test_modelos()
    sys.exit(0 if resultados['errores'] == 0 else 1)
