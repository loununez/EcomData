# Carpeta de Testing - EcomData

Esta carpeta contiene la suite completa de testing para la aplicación EcomData.

## Estructura

```
test/
├── __init__.py                 # Inicializador del módulo
├── run_all_tests.py            # Script maestro (ejecutar esto)
├── test_syntax.py              # Prueba de sintaxis Python
├── test_dependencies.py         # Prueba de dependencias
├── test_models.py              # Prueba de modelos ORM
├── test_app_config.py          # Prueba de configuración de app
├── test_database.py            # Prueba de base de datos
├── testing.md                  # Guía completa de testing
├── informe.md                  # Informe detallado del último testing
└── README.md                   # Este archivo
```

## Inicio Rápido

### Ejecutar Todos los Tests

```powershell
cd c:\Users\skupe\Desktop\app\EcomData
python test/run_all_tests.py
```

### Ejecutar un Test Individual

```powershell
python test/test_syntax.py
python test/test_dependencies.py
python test/test_models.py
python test/test_app_config.py
python test/test_database.py
```

## Descripción de Tests

| Script | Propósito | Tiempo |
|--------|-----------|--------|
| test_syntax.py | Verifica sintaxis de 89 archivos Python | ~2s |
| test_dependencies.py | Valida dependencias externas e internas | ~1s |
| test_models.py | Prueba 12 modelos ORM | ~1s |
| test_app_config.py | Verifica 24 blueprints | ~1s |
| test_database.py | Valida integridad de BD | ~1s |

## Resultados Esperados

Todos los tests deben mostrar:
```
[OK] - Verificación de sintaxis Python
[OK] - Análisis de dependencias
[OK] - Integridad de modelos
[OK] - Configuración de aplicación
[OK] - Pruebas de base de datos

Resultado final: 5/5 pruebas exitosas
[OK] TODAS LAS PRUEBAS PASARON EXITOSAMENTE
```

## Archivo de Informe

El archivo `informe.md` contiene el reporte completo del último testing incluyendo:
- Resumen ejecutivo
- Resultados detallados por prueba
- Listado de archivos validados
- Listado de modelos y blueprints
- Recomendaciones
- Checklist de verificación manual

## Documentación Completa

Ver `testing.md` para la guía completa de testing incluyendo:
- Descripción detallada de cada test
- Cómo interpretar resultados
- Solución de problemas comunes
- Mejores prácticas
- Verificación manual adicional

## Notas Importantes

1. **Base de Datos:** Si no existe `ecomdata.db`, ejecutar:
   ```powershell
   python init_db.py
   ```

2. **Encoding:** Los tests están configurados para UTF-8 en Windows

3. **Frecuencia:** Ejecutar tests:
   - Después de cambios importantes
   - Antes de hacer commit
   - Antes de desplegar

4. **Fallos:** Si algún test falla, revisar `testing.md` sección "Solución de Problemas"

## Contacto

Para problemas o preguntas sobre los tests, revisar:
1. Archivo `testing.md` - Guía completa
2. Archivo `informe.md` - Últimos resultados
3. Logs de cada test individual

---

**Última actualización:** 18 de Noviembre de 2025  
**Versión:** 1.0.0
