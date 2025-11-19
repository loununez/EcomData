"""
Script para verificar la configuración de la aplicación Quart.
Valida que la aplicación se cree correctamente y que todos los blueprints estén registrados.
"""

import sys
import os

# Configurar encoding UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import app as app_module
except Exception as e:
    print(f"Error al importar la aplicación: {e}")
    sys.exit(1)


def test_app_creation():
    """Prueba que la aplicación Quart se cree correctamente"""
    print("\n" + "="*70)
    print("PRUEBA DE CREACIÓN DE APLICACIÓN")
    print("="*70 + "\n")
    
    try:
        aplicacion = app_module.app
        print(f"✓ Aplicación Quart creada correctamente")
        print(f"  - Nombre: {aplicacion.name}")
        print(f"  - Debug: {aplicacion.debug}")
        return True
    except Exception as e:
        print(f"✗ Error al crear la aplicación: {e}")
        return False


def test_blueprints():
    """Prueba que todos los blueprints estén registrados"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE BLUEPRINTS REGISTRADOS")
    print("="*70 + "\n")
    
    try:
        aplicacion = app_module.app
        blueprints = aplicacion.blueprints
        
        print(f"Total de blueprints: {len(blueprints)}\n")
        
        BLUEPRINTS_ESPERADOS = [
            'auth', 'administracion', 'catalogo_categorias', 'catalogo_productos',
            'clientes', 'configuracion_general', 'configuracion_notificaciones',
            'configuracion_seguridad', 'inicio', 'inventario', 'inventario_agregar',
            'nueva_categoria', 'nuevo_producto', 'pagos', 'pagos_nuevo_pago',
            'panel', 'reportes', 'usuarios', 'usuarios_agregar', 'ventas', 'ventas_carrito',
            'analisis_negocio_clientes', 'analisis_negocio_productos', 'analisis_negocio_resumen'
        ]
        
        exitosos = 0
        faltantes = []
        
        for blueprint_nombre in sorted(blueprints.keys()):
            if blueprint_nombre in BLUEPRINTS_ESPERADOS:
                print(f"✓ {blueprint_nombre}")
                exitosos += 1
            else:
                print(f"? {blueprint_nombre} (no esperado)")
                exitosos += 1
        
        for esperado in BLUEPRINTS_ESPERADOS:
            if esperado not in blueprints:
                print(f"✗ {esperado} (FALTANTE)")
                faltantes.append(esperado)
        
        print("\n" + "="*70)
        if faltantes:
            print(f"Resultado: {exitosos} blueprints cargados, {len(faltantes)} faltantes")
        else:
            print(f"Resultado: {exitosos} blueprints cargados correctamente")
        print("="*70 + "\n")
        
        return len(faltantes) == 0
    except Exception as e:
        print(f"✗ Error al verificar blueprints: {e}")
        return False


def test_static_folder():
    """Prueba que la carpeta estática exista"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE CARPETAS ESTÁTICAS")
    print("="*70 + "\n")
    
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpetas = {
        'static': os.path.join(app_dir, 'static'),
        'templates': os.path.join(app_dir, 'templates'),
        'database': os.path.join(app_dir, 'database'),
        'models': os.path.join(app_dir, 'models'),
        'modules': os.path.join(app_dir, 'modules'),
    }
    
    resultados = {'existentes': 0, 'faltantes': []}
    
    for nombre, ruta in carpetas.items():
        if os.path.isdir(ruta):
            print(f"✓ {nombre}: {ruta}")
            resultados['existentes'] += 1
        else:
            print(f"✗ {nombre}: NO ENCONTRADO")
            resultados['faltantes'].append(nombre)
    
    print("\n" + "="*70)
    print(f"Resultado: {resultados['existentes']} carpetas OK, {len(resultados['faltantes'])} faltantes")
    print("="*70 + "\n")
    
    return len(resultados['faltantes']) == 0


def main():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*70)
    print("PRUEBA DE CONFIGURACIÓN DE APLICACIÓN")
    print("="*70)
    
    resultados = {
        'app': test_app_creation(),
        'blueprints': test_blueprints(),
        'folders': test_static_folder(),
    }
    
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"Aplicación: {'✓ OK' if resultados['app'] else '✗ ERROR'}")
    print(f"Blueprints: {'✓ OK' if resultados['blueprints'] else '✗ ERROR'}")
    print(f"Carpetas: {'✓ OK' if resultados['folders'] else '✗ ERROR'}")
    print("="*70 + "\n")
    
    exito = all(resultados.values())
    return exito


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
