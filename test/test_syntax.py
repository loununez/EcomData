"""
Script para verificar la sintaxis de todos los archivos Python.
Detecta errores de compilación en los módulos de la aplicación.
"""

import os
import py_compile
import sys
from pathlib import Path

# Configurar encoding UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


def obtener_archivos_python(directorio_raiz, excluir=['__pycache__', '.git', 'venv', 'env']):
    """Obtiene todos los archivos Python del proyecto"""
    archivos = []
    
    for raiz, dirs, archivos_en_dir in os.walk(directorio_raiz):
        # Eliminar directorios a excluir
        dirs[:] = [d for d in dirs if d not in excluir]
        
        for archivo in archivos_en_dir:
            if archivo.endswith('.py'):
                ruta_completa = os.path.join(raiz, archivo)
                archivos.append(ruta_completa)
    
    return sorted(archivos)


def verificar_sintaxis_archivo(ruta_archivo):
    """Verifica la sintaxis de un archivo Python"""
    try:
        py_compile.compile(ruta_archivo, doraise=True)
        return True, None
    except py_compile.PyCompileError as e:
        return False, str(e)


def main():
    """Ejecuta la verificación de sintaxis en todos los archivos"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE SINTAXIS DE ARCHIVOS PYTHON")
    print("="*70 + "\n")
    
    directorio_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    archivos_python = obtener_archivos_python(directorio_raiz)
    
    print(f"Total de archivos Python encontrados: {len(archivos_python)}\n")
    
    resultados = {
        'exitosos': 0,
        'errores': [],
        'detalles': []
    }
    
    for archivo in archivos_python:
        # Obtener ruta relativa para mejor presentación
        ruta_relativa = os.path.relpath(archivo, directorio_raiz)
        
        exito, error = verificar_sintaxis_archivo(archivo)
        
        if exito:
            resultados['exitosos'] += 1
            print(f"✓ {ruta_relativa}")
        else:
            resultados['errores'].append((ruta_relativa, error))
            print(f"✗ {ruta_relativa}")
            if error:
                # Mostrar primeras líneas del error
                lineas_error = error.split('\n')[:3]
                for linea in lineas_error:
                    print(f"    {linea}")
    
    print("\n" + "="*70)
    print("RESUMEN")
    print("="*70)
    print(f"Archivos OK: {resultados['exitosos']}")
    print(f"Archivos con errores: {len(resultados['errores'])}")
    
    if resultados['errores']:
        print("\nArchivos con errores:")
        for archivo, error in resultados['errores']:
            print(f"  - {archivo}")
    
    print("="*70 + "\n")
    
    exito = len(resultados['errores']) == 0
    return exito


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
