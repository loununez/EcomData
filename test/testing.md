# Guía de Testing - EcomData

## Descripción General

Este documento proporciona instrucciones completas sobre cómo ejecutar las pruebas de la aplicación EcomData. La suite de testing verifica la integridad, configuración y funcionalidad de toda la aplicación.

## Estructura de Tests

La carpeta `test/` contiene los siguientes scripts:

### 1. `test_syntax.py`
**Propósito:** Verifica la sintaxis de todos los archivos Python del proyecto.

**Qué valida:**
- Compila todos los archivos `.py` en el directorio de la aplicación
- Detecta errores de sintaxis
- Verifica que los archivos sean válidos para Python

**Ejecución:**
```powershell
cd c:\Users\skupe\Desktop\app\EcomData
python test/test_syntax.py
```

**Resultado esperado:**
- ✓ Todos los archivos Python compilados correctamente
- Listado de todos los archivos validados

---

### 2. `test_dependencies.py`
**Propósito:** Verifica que todas las dependencias externas estén instaladas.

**Qué valida:**
- Existencia de paquetes requeridos: Quart, SQLAlchemy, Werkzeug, Jinja2, aiosqlite
- Importación correcta de todos los módulos internos
- Integridad de las importaciones

**Dependencias verificadas:**
- `quart` - Framework web asincrónico
- `sqlalchemy` - ORM para base de datos
- `werkzeug` - Utilidades web y seguridad
- `jinja2` - Motor de templates
- `aiosqlite` - Driver asincrónico SQLite

**Ejecución:**
```powershell
python test/test_dependencies.py
```

**Resultado esperado:**
- ✓ Todas las dependencias externas disponibles
- ✓ Todos los módulos internos importados correctamente

---

### 3. `test_models.py`
**Propósito:** Verifica que todos los modelos de datos se carguen correctamente.

**Qué valida:**
- Carga de todas las clases modelo
- Existencia de `__tablename__` en cada modelo
- Integridad estructural de los modelos

**Modelos validados:**
- Usuario
- Rol
- Producto
- Categoría
- Cliente
- Pago
- Venta
- DetalleVenta
- Inventario
- Configuración

**Ejecución:**
```powershell
python test/test_models.py
```

**Resultado esperado:**
- ✓ Todos los modelos cargados correctamente
- Listado de atributos por modelo

---

### 4. `test_app_config.py`
**Propósito:** Verifica la configuración y estructura de la aplicación Quart.

**Qué valida:**
- Creación correcta de la instancia de Quart
- Registro de todos los blueprints
- Existencia de carpetas requeridas (static, templates, database, models, modules)

**Blueprints verificados:**
- auth, administracion, catalogo_categorias, catalogo_productos
- clientes, configuracion_general, configuracion_notificaciones, configuracion_seguridad
- inicio, inventario, inventario_agregar, nueva_categoria
- nuevo_producto, pagos, pagos_nuevo_pago, panel
- reportes, usuarios, usuarios_agregar, ventas
- ventas_carrito, analisis_negocio_clientes, analisis_negocio_productos, analisis_negocio_resumen

**Ejecución:**
```powershell
python test/test_app_config.py
```

**Resultado esperado:**
- ✓ Aplicación Quart creada correctamente
- ✓ Todos los blueprints registrados
- ✓ Todas las carpetas requeridas existen

---

### 5. `test_database.py`
**Propósito:** Verifica la integridad de la base de datos SQLite.

**Qué valida:**
- Conexión exitosa a `ecom_data.db`
- Existencia de todas las tablas requeridas
- Integridad referencial de la base de datos
- Estado de las llaves foráneas

**Tablas validadas:**
- rol, usuario, categoria, producto, cliente
- venta, detalle_venta, pago, inventario, configuracion

**Ejecución:**
```powershell
python test/test_database.py
```

**Resultado esperado:**
- ✓ Conexión a base de datos exitosa
- ✓ Todas las tablas existen
- ✓ Integridad de base de datos OK

---

## Ejecución de Tests

### Opción 1: Ejecutar un test individual

```powershell
# Ejemplo: Verificar sintaxis
python test/test_syntax.py

# Ejemplo: Verificar dependencias
python test/test_dependencies.py
```

### Opción 2: Ejecutar todos los tests (RECOMENDADO)

```powershell
# Ejecutar suite completa
python test/run_all_tests.py
```

Este comando ejecuta todos los tests en orden y proporciona un resumen final.

### Opción 3: Ejecutar desde PowerShell con bucle

```powershell
$tests = @(
    "test_syntax.py",
    "test_dependencies.py",
    "test_models.py",
    "test_app_config.py",
    "test_database.py"
)

foreach ($test in $tests) {
    Write-Host "`n=== Ejecutando $test ===" -ForegroundColor Cyan
    python test/$test
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Test falló: $test" -ForegroundColor Red
    } else {
        Write-Host "✓ Test pasó: $test" -ForegroundColor Green
    }
}
```

---

## Interpretación de Resultados

### Códigos de Salida

- **0**: Todas las pruebas pasaron exitosamente ✓
- **1**: Una o más pruebas fallaron ✗

### Símbolos en los Reportes

- **✓** : Prueba o componente exitoso
- **✗** : Prueba o componente fallido
- **?** : Componente no esperado o información adicional

### Ejemplo de Salida Exitosa

```
======================================================================
RESUMEN DE PRUEBAS
======================================================================

✓ PASS - Verificación de sintaxis Python
✓ PASS - Análisis de dependencias
✓ PASS - Integridad de modelos
✓ PASS - Configuración de aplicación
✓ PASS - Pruebas de base de datos

======================================================================
Resultado final: 5/5 pruebas exitosas
✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE
======================================================================
```

---

## Solución de Problemas Comunes

### Error: "Import 'quart' could not be resolved"

**Causa:** Quart no está instalado

**Solución:**
```powershell
pip install -r requirements.txt
```

### Error: "Base de datos no encontrada"

**Causa:** El archivo `ecom_data.db` no existe

**Solución:**
```powershell
cd c:\Users\skupe\Desktop\app\EcomData
python database/__init__db.py
```

### Error: "Módulo no encontrado"

**Causa:** El PYTHONPATH no está configurado correctamente

**Solución:**
Asegúrese de ejecutar los tests desde la carpeta raíz de la aplicación:
```powershell
cd c:\Users\skupe\Desktop\app\EcomData
python test/test_dependencies.py
```

### Error: "Select no tiene título de acceso"

**Causa:** Advertencia de accesibilidad en HTML (no es un error crítico)

**Solución:** Ignorar - Esta es una advertencia de linting, no afecta la funcionalidad

---

## Mejores Prácticas

1. **Ejecutar tests regularmente**: Especialmente después de cambios en el código
2. **Ejecutar antes de desplegar**: Siempre run `run_all_tests.py` antes de hacer deploy
3. **Revisar logs**: Revise los detalles de cualquier error reportado
4. **Mantener base de datos**: Asegúrese que `ecom_data.db` esté presente
5. **Verificar dependencias**: Mantenga `requirements.txt` actualizado

---

## Verificación Manual Adicional

Si todos los tests automáticos pasan, puede realizar verificaciones manuales:

### 1. Verificar la aplicación se inicia
```powershell
py -3.11 app.py
```

### 2. Acceder a la aplicación
```
http://127.0.0.1:5000/
```

### 3. Verificar login
- Usuario: `admin`
- Contraseña: (según la que haya establecido)

### 4. Navegar por módulos
- Usuarios: http://127.0.0.1:5000/usuarios/
- Productos: http://127.0.0.1:5000/catalogo_productos/
- Clientes: http://127.0.0.1:5000/clientes/
- Pagos: http://127.0.0.1:5000/pagos/

---

## Contacto y Soporte

Para problemas o preguntas sobre los tests, revise:
1. El archivo `informe.md` con el último reporte de testing
2. Los logs específicos de cada test
3. La documentación del proyecto

---

**Última actualización:** Noviembre 18, 2025
**Versión de testing:** 1.0.0
