"""
Script para verificar la integridad de la base de datos.
Valida que todas las tablas existan y sean accesibles.
"""

import sqlite3
import os
import sys

# Configurar encoding UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


def test_database_connection():
    """Prueba la conexión a la base de datos"""
    print("\n" + "="*70)
    print("PRUEBA DE CONEXIÓN A BASE DE DATOS")
    print("="*70 + "\n")
    
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ecomdata.db')
    
    if not os.path.exists(db_path):
        print(f"✗ Base de datos no encontrada: {db_path}")
        return False, None
    
    try:
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()[0]
        print(f"✓ Conexión exitosa a SQLite")
        print(f"  - Versión: {version}")
        print(f"  - Archivo: {db_path}")
        return True, conexion
    except Exception as e:
        print(f"✗ Error de conexión: {e}")
        return False, None


def test_database_tables(conexion):
    """Verifica que todas las tablas esperadas existan"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE TABLAS EN BASE DE DATOS")
    print("="*70 + "\n")
    
    TABLAS_ESPERADAS = [
        'roles', 'usuarios', 'categorias', 'productos', 'clientes', 
        'ventas', 'detalle_ventas', 'pagos', 'inventario', 
        'configuracion_general', 'configuracion_notificaciones', 'configuracion_seguridad'
    ]
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas_existentes = [tabla[0] for tabla in cursor.fetchall()]
        
        exitosas = 0
        faltantes = []
        extra = []
        
        for tabla in TABLAS_ESPERADAS:
            if tabla in tablas_existentes:
                cursor.execute(f"PRAGMA table_info({tabla})")
                columnas = cursor.fetchall()
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                registros = cursor.fetchone()[0]
                print(f"✓ {tabla}: {len(columnas)} columnas, {registros} registros")
                exitosas += 1
            else:
                print(f"✗ {tabla}: NO ENCONTRADA")
                faltantes.append(tabla)
        
        for tabla in tablas_existentes:
            if tabla not in TABLAS_ESPERADAS:
                print(f"? {tabla}: tabla extra encontrada")
                extra.append(tabla)
        
        print("\n" + "="*70)
        print(f"Resultado: {exitosas} tablas OK, {len(faltantes)} faltantes, {len(extra)} extras")
        print("="*70 + "\n")
        
        return len(faltantes) == 0
    except Exception as e:
        print(f"✗ Error al verificar tablas: {e}")
        return False


def test_table_integrity(conexion):
    """Verifica la integridad de las tablas"""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE INTEGRIDAD DE TABLAS")
    print("="*70 + "\n")
    
    try:
        cursor = conexion.cursor()
        
        # Ejecutar PRAGMA integrity_check
        cursor.execute("PRAGMA integrity_check(100)")
        resultado = cursor.fetchone()[0]
        
        if resultado == "ok":
            print("✓ Integridad de base de datos: OK")
            print("  - No se encontraron problemas de corrupción")
        else:
            print(f"✗ Problemas detectados: {resultado}")
            return False
        
        # Verificar foreign keys
        cursor.execute("PRAGMA foreign_keys")
        fk_enabled = cursor.fetchone()[0]
        print(f"✓ Foreign Keys: {'Habilitadas' if fk_enabled else 'Deshabilitadas'}")
        
        print("\n" + "="*70 + "\n")
        return True
    except Exception as e:
        print(f"✗ Error al verificar integridad: {e}")
        return False


def main():
    """Ejecuta todas las pruebas de base de datos"""
    print("\n" + "="*70)
    print("PRUEBAS DE BASE DE DATOS")
    print("="*70)
    
    conexion_ok, conexion = test_database_connection()
    
    if not conexion_ok:
        print("\n✗ No se pudo conectar a la base de datos. Abortando pruebas.")
        return False
    
    try:
        tablas_ok = test_database_tables(conexion)
        integridad_ok = test_table_integrity(conexion)
        
        print("="*70)
        print("RESUMEN DE PRUEBAS DE BASE DE DATOS")
        print("="*70)
        print(f"Conexión: ✓ OK")
        print(f"Tablas: {'✓ OK' if tablas_ok else '✗ ERROR'}")
        print(f"Integridad: {'✓ OK' if integridad_ok else '✗ ERROR'}")
        print("="*70 + "\n")
        
        exito = tablas_ok and integridad_ok
        return exito
    finally:
        conexion.close()


if __name__ == '__main__':
    exito = main()
    sys.exit(0 if exito else 1)
