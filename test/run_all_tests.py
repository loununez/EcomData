"""
Script maestro para ejecutar todas las pruebas de la aplicación.
Coordina la ejecución de todos los test scripts y genera un reporte consolidado.
"""

import subprocess
import sys
import os
from datetime import datetime

# Configurar encoding UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def ejecutar_test(nombre_script, descripcion):
    """Ejecuta un script de test y retorna el resultado"""
    print("\n" + "-"*70)
    print(f"Ejecutando: {descripcion}")
    print(f"Script: {nombre_script}")
    print("-"*70)
    
    ruta_script = os.path.join(os.path.dirname(__file__), nombre_script)
    
    try:
        resultado = subprocess.run(
            [sys.executable, ruta_script],
            capture_output=False,
            timeout=60
        )
        exito = resultado.returncode == 0
        return {
            'nombre': nombre_script,
            'descripcion': descripcion,
            'exito': exito,
            'codigo_salida': resultado.returncode
        }
    except subprocess.TimeoutExpired:
        print(f"✗ El test tardó demasiado (timeout 60s)")
        return {
            'nombre': nombre_script,
            'descripcion': descripcion,
            'exito': False,
            'codigo_salida': -1
        }
    except Exception as e:
        print(f"✗ Error al ejecutar el test: {e}")
        return {
            'nombre': nombre_script,
            'descripcion': descripcion,
            'exito': False,
            'codigo_salida': -2
        }


def main():
    """Ejecuta todos los tests"""
    print("\n" + "="*70)
    print("SUITE DE PRUEBAS - EcomData")
    print("="*70)
    print(f"Fecha/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*70)
    
    tests = [
        ('test_syntax.py', 'Verificación de sintaxis Python'),
        ('test_dependencies.py', 'Análisis de dependencias'),
        ('test_models.py', 'Integridad de modelos'),
        ('test_app_config.py', 'Configuración de aplicación'),
        ('test_database.py', 'Pruebas de base de datos'),
    ]
    
    resultados = []
    
    for nombre_script, descripcion in tests:
        resultado = ejecutar_test(nombre_script, descripcion)
        resultados.append(resultado)
    
    # Mostrar resumen
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70 + "\n")
    
    exitosos = sum(1 for r in resultados if r['exito'])
    totales = len(resultados)
    
    for resultado in resultados:
        estado = "[OK]" if resultado['exito'] else "[FAIL]"
        print(f"{estado} - {resultado['descripcion']}")
    
    print("\n" + "="*70)
    print(f"Resultado final: {exitosos}/{totales} pruebas exitosas")
    
    if exitosos == totales:
        print("[OK] TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*70 + "\n")
        return True
    else:
        print(f"[FAIL] {totales - exitosos} prueba(s) fallaron")
        print("="*70 + "\n")
        return False


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
