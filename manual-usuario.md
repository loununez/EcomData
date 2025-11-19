# Manual de Usuario - EcomData

**Versión:** 1.0.0  
**Fecha:** Noviembre 2025  
**Idioma:** Español  
**Público:** Usuarios del Sistema de Gestión EcomData

---

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Acceso al Sistema](#acceso-al-sistema)
4. [Interfaz Principal](#interfaz-principal)
5. [Módulos del Sistema](#módulos-del-sistema)
6. [Gestión de Usuarios](#gestión-de-usuarios)
7. [Gestión de Productos](#gestión-de-productos)
8. [Gestión de Clientes](#gestión-de-clientes)
9. [Gestión de Ventas](#gestión-de-ventas)
10. [Gestión de Pagos](#gestión-de-pagos)
11. [Gestión de Inventario](#gestión-de-inventario)
12. [Reportes y Análisis](#reportes-y-análisis)
13. [Configuración del Sistema](#configuración-del-sistema)
14. [Preguntas Frecuentes](#preguntas-frecuentes)
15. [Contacto y Soporte](#contacto-y-soporte)

---

## Introducción

### ¿Qué es EcomData?

EcomData es un **Sistema de Gestión Integral** diseñado para administrar todos los aspectos de un negocio de comercio electrónico, incluyendo:

- Gestión de usuarios y roles
- Catálogo de productos y categorías
- Base de clientes
- Registro de ventas
- Control de pagos
- Inventario y stock
- Reportes y análisis de negocio

### Características Principales

✓ Interfaz intuitiva y fácil de usar  
✓ Acceso seguro con autenticación  
✓ Múltiples roles de usuario  
✓ Indicadores en tiempo real  
✓ Reportes detallados  
✓ Base de datos confiable  
✓ Respaldo automático de datos

---

## Requisitos del Sistema

### Hardware Mínimo

- Procesador: Intel Core i3 o equivalente
- RAM: 4 GB
- Disco Duro: 500 MB libres
- Conexión a Internet: ADSL o superior

### Software Requerido

- Navegador Web: Chrome, Firefox, Edge o Safari (versión reciente)
- Sistema Operativo: Windows 7+, macOS 10.12+, Linux (cualquier distribución)
- JavaScript: Habilitado en el navegador

### Navegadores Recomendados

| Navegador | Versión Mínima | Estado |
|-----------|-----------------|--------|
| Google Chrome | 90+ | ✓ Recomendado |
| Firefox | 88+ | ✓ Compatible |
| Microsoft Edge | 90+ | ✓ Compatible |
| Safari | 14+ | ✓ Compatible |

---

## Acceso al Sistema

### Iniciando Sesión

1. **Abrir el Navegador**
   - Accede a: `http://127.0.0.1:5000/`
   - O la URL proporcionada por tu administrador

2. **Pantalla de Login**
   ```
   [ESPACIO PARA SCREENSHOT DE LOGIN]
   ```
   - Ingresa tu **Usuario**
   - Ingresa tu **Contraseña**
   - Haz clic en **"Iniciar Sesión"**

3. **Recuperar Contraseña**
   - Si olvidaste tu contraseña, contacta al administrador del sistema
   - No compartas tu contraseña con nadie

### Cierre de Sesión

Para salir del sistema:
1. Busca tu nombre de usuario en la esquina superior derecha
2. Haz clic en **"Cerrar Sesión"**
3. Confirma la acción si es necesario

### Seguridad de Acceso

⚠️ **Recomendaciones Importantes:**
- Nunca compartas tu contraseña
- Cambia tu contraseña regularmente
- Cierra sesión cuando termines de usar el sistema
- No dejes el navegador abierto en equipo compartido
- Usa una conexión segura (preferentemente VPN en redes públicas)

---

## Interfaz Principal

### Estructura de la Pantalla

```
[ESPACIO PARA SCREENSHOT DE INTERFAZ PRINCIPAL]

┌─────────────────────────────────────────────────────────┐
│  LOGO  │    Bienvenido, [Usuario]   │ ⚙️ Configuración  │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Menú Lateral                    │  Área Principal       │
│  ├─ Inicio                       │                       │
│  ├─ Usuarios                     │  [Contenido dinámico] │
│  ├─ Productos                    │                       │
│  ├─ Clientes                     │                       │
│  ├─ Ventas                       │                       │
│  ├─ Pagos                        │                       │
│  ├─ Inventario                   │                       │
│  ├─ Reportes                     │                       │
│  └─ Configuración                │                       │
└─────────────────────────────────────────────────────────┘
```

### Elementos Principales

#### Barra de Navegación Superior
- **Logo del Sistema:** Haz clic para ir a Inicio
- **Nombre de Usuario:** Muestra tu usuario actual
- **Menú de Usuario:** Acceso a perfil y configuración
- **Notificaciones:** Alertas del sistema (si las hay)

#### Menú Lateral
- **Navegación Principal:** Accede a todos los módulos
- **Módulos Activos:** Se resaltan en color
- **Contraer/Expandir:** Comprime el menú para más espacio
- **Búsqueda:** Encuentra módulos rápidamente

#### Área de Contenido
- **Panel Principal:** Muestra información del módulo actual
- **Barra de Herramientas:** Acciones disponibles (Crear, Editar, Eliminar)
- **Tablas de Datos:** Listado de registros
- **Formularios:** Para ingresar información

---

## Módulos del Sistema

### Acceso a Módulos

Para acceder a cualquier módulo:

1. **Desde el Menú Lateral**
   ```
   [ESPACIO PARA SCREENSHOT DEL MENÚ]
   ```
   - Haz clic en el nombre del módulo que deseas

2. **Desde el Inicio**
   - Accede a módulos frecuentes desde tarjetas de inicio rápido

3. **Mediante Búsqueda**
   - Usa la búsqueda del menú para encontrar módulos

### Módulos Disponibles

| Módulo | Función | Acceso |
|--------|---------|--------|
| **Usuarios** | Gestionar usuarios del sistema | `/usuarios` |
| **Productos** | Administrar catálogo de productos | `/catalogo_productos` |
| **Clientes** | Gestionar base de clientes | `/clientes` |
| **Ventas** | Registrar y administrar ventas | `/ventas` |
| **Pagos** | Control de pagos y dinero recibido | `/pagos` |
| **Inventario** | Gestión de stock y almacén | `/inventario` |
| **Reportes** | Análisis y reportes del negocio | `/reportes` |
| **Configuración** | Ajustes del sistema | `/configuracion_general` |

---

## Gestión de Usuarios

### Acceder al Módulo de Usuarios

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO USUARIOS]
```

**Ruta:** Menú Lateral → Usuarios

### Vista de Usuarios

La pantalla muestra una tabla con todos los usuarios registrados:

| Columna | Descripción |
|---------|------------|
| **Usuario** | Nombre de usuario para acceder |
| **Rol** | Función del usuario (Administrador, Vendedor, etc.) |
| **Estado** | Activo o Inactivo |
| **Fecha Registro** | Cuándo se creó la cuenta |
| **Acciones** | Editar o Eliminar |

### Filtrar Usuarios

1. **Por Nombre o Email**
   - Escribe en el campo de búsqueda
   - Los resultados se filtran automáticamente

2. **Por Rol**
   - Selecciona un rol del desplegable
   - Muestra solo usuarios con ese rol

3. **Por Estado**
   - Filtrar usuarios activos o inactivos

### Crear Nuevo Usuario

1. Haz clic en **"Agregar Usuario"** o **"Nuevo Usuario"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO CREAR USUARIO]
   ```

2. Completa los campos requeridos:
   - **Nombre Completo:** Nombre real del usuario
   - **Email:** Correo electrónico válido
   - **Usuario:** Nombre para login (sin espacios)
   - **Contraseña:** Mínimo 8 caracteres
   - **Rol:** Selecciona el rol del usuario
   - **Estado:** Activo/Inactivo

3. Haz clic en **"Guardar"**

4. Verás un mensaje de confirmación

### Editar Usuario

1. En la tabla, busca el usuario
2. Haz clic en el botón **Editar** (✏️ lápiz)
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO EDITAR USUARIO]
   ```
3. Modifica los campos que necesites
4. Haz clic en **"Guardar Cambios"**

### Eliminar Usuario

1. Busca el usuario en la tabla
2. Haz clic en el botón **Eliminar** (🗑️ papelera)
3. **Confirma** que deseas eliminar
   ```
   [ESPACIO PARA SCREENSHOT DE CONFIRMACIÓN]
   ```
4. El usuario se eliminará del sistema

⚠️ **Nota:** La eliminación es permanente y no se puede deshacer.

---

## Gestión de Productos

### Acceder al Módulo de Productos

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO PRODUCTOS]
```

**Ruta:** Menú Lateral → Productos (o Catálogo de Productos)

### Vista de Productos

Tabla con listado de productos disponibles:

| Columna | Descripción |
|---------|------------|
| **Nombre** | Nombre del producto |
| **Descripción** | Detalles del producto |
| **Categoría** | Tipo/Categoría del producto |
| **Precio** | Precio de venta |
| **Stock** | Cantidad disponible |
| **Acciones** | Editar o Eliminar |

### Filtrar Productos

1. **Por Nombre**
   - Escribe en el campo de búsqueda
   - Busca por nombre del producto

2. **Por Categoría**
   - Selecciona una categoría del desplegable
   - Muestra solo productos de esa categoría

3. **Por Stock**
   - Filtrar por disponibilidad (Bajo, Medio, Alto)

### Crear Nuevo Producto

1. Haz clic en **"Agregar Producto"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO CREAR PRODUCTO]
   ```

2. Completa los campos:
   - **Nombre:** Nombre del producto
   - **Descripción:** Detalles y características
   - **Categoría:** Selecciona una categoría existente
   - **Precio:** Precio de venta ($)
   - **Stock Inicial:** Cantidad disponible
   - **SKU/Código:** Identificador único (opcional)

3. Haz clic en **"Guardar"**

### Editar Producto

1. Busca el producto en la tabla
2. Haz clic en el botón **Editar** (✏️)
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO EDITAR PRODUCTO]
   ```
3. Modifica los datos necesarios
4. Haz clic en **"Guardar Cambios"**

### Eliminar Producto

1. Busca el producto
2. Haz clic en **Eliminar** (🗑️)
3. Confirma la eliminación

### Crear Nueva Categoría

1. Haz clic en **"Nueva Categoría"**
   ```
   [ESPACIO PARA SCREENSHOT DE MODAL NUEVA CATEGORÍA]
   ```

2. Ingresa el nombre de la categoría
3. Haz clic en **"Crear"**

---

## Gestión de Clientes

### Acceder al Módulo de Clientes

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO CLIENTES]
```

**Ruta:** Menú Lateral → Clientes

### Vista de Clientes

Tabla con información de clientes:

| Columna | Descripción |
|---------|------------|
| **Cliente** | Nombre del cliente |
| **Estado** | Activo o Inactivo |
| **Teléfono** | Número de contacto |
| **Dirección** | Domicilio del cliente |
| **Fecha Registro** | Cuándo se registró |
| **Acciones** | Editar o Eliminar |

### Filtrar Clientes

1. **Por Nombre o Email**
   - Busca en el campo de texto

2. **Por Estado**
   - Activos o Inactivos

### Crear Nuevo Cliente

1. Haz clic en **"Agregar Cliente"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO CREAR CLIENTE]
   ```

2. Completa los datos:
   - **Nombre Completo:** Nombre del cliente
   - **Email:** Correo electrónico
   - **Teléfono:** Número de contacto
   - **Dirección:** Domicilio
   - **Ciudad:** Ciudad de residencia
   - **Estado:** Activo/Inactivo

3. Haz clic en **"Guardar"**

### Editar Cliente

1. Busca el cliente en la tabla
2. Haz clic en **Editar** (✏️)
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO EDITAR CLIENTE]
   ```
3. Actualiza la información
4. Haz clic en **"Guardar Cambios"**

### Eliminar Cliente

1. Busca el cliente
2. Haz clic en **Eliminar** (🗑️)
3. Confirma la acción

---

## Gestión de Ventas

### Acceder al Módulo de Ventas

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO VENTAS]
```

**Ruta:** Menú Lateral → Ventas

### Vista de Ventas

Tabla con registro de ventas realizadas:

| Columna | Descripción |
|---------|------------|
| **ID Venta** | Identificador único |
| **Cliente** | Quién realizó la compra |
| **Total** | Monto de la venta |
| **Fecha** | Cuándo se realizó |
| **Estado** | Completada o Pendiente |
| **Acciones** | Ver detalles |

### Indicadores de Ventas

En la parte superior de la pantalla, verás indicadores:

```
[ESPACIO PARA SCREENSHOT DE INDICADORES]
```

- **Total Hoy:** Total de ventas del día actual
- **Ventas Completadas:** Número de transacciones
- **Ticket Promedio:** Monto promedio por venta
- **Cliente Frecuente:** Mejor cliente

### Crear Nueva Venta

1. Haz clic en **"Nueva Venta"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO NUEVA VENTA]
   ```

2. Selecciona el **Cliente**

3. Agrega **Productos:**
   - Selecciona el producto
   - Ingresa cantidad
   - Haz clic en **"Agregar al Carrito"**

4. Revisa el **Resumen:**
   - Subtotal
   - Descuentos (si aplica)
   - Total a pagar

5. Haz clic en **"Completar Venta"**

### Ver Detalles de Venta

1. En la tabla, busca la venta
2. Haz clic en **"Ver Detalles"**
   ```
   [ESPACIO PARA SCREENSHOT DE DETALLES VENTA]
   ```

3. Verás:
   - Información del cliente
   - Productos comprados
   - Montos y impuestos
   - Fecha y hora de la venta

---

## Gestión de Pagos

### Acceder al Módulo de Pagos

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO PAGOS]
```

**Ruta:** Menú Lateral → Pagos

### Indicadores de Pagos

En la parte superior, verás datos en tiempo real:

```
[ESPACIO PARA SCREENSHOT DE INDICADORES DE PAGOS]
```

- **Total Hoy:** Dinero recibido hoy
- **Efectivo Hoy:** Dinero en efectivo del día
- **Total Efectivo:** Efectivo acumulado (histórico)
- **Tarjetas Hoy:** Dinero por tarjeta del día

### Vista de Pagos

Tabla con registro de todos los pagos:

| Columna | Descripción |
|---------|------------|
| **Venta** | Número de la venta |
| **Monto** | Cantidad pagada |
| **Método** | Efectivo, Tarjeta, Transferencia |
| **Cliente** | Quién realizó el pago |
| **Fecha** | Cuándo se registró |
| **Acciones** | Editar o Eliminar |

### Filtrar Pagos

1. **Por Búsqueda**
   - Busca por número de venta o cliente

2. **Por Método de Pago**
   - Selecciona: Efectivo, Tarjeta o Transferencia

### Registrar Nuevo Pago

1. Haz clic en **"Nuevo Pago"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO NUEVO PAGO]
   ```

2. Selecciona la **Venta** pendiente de pago

3. Ingresa los datos:
   - **Monto:** Cantidad pagada
   - **Método:** Tipo de pago
   - **Referencia:** Número de operación (opcional)

4. Haz clic en **"Registrar Pago"**

### Editar Pago

1. Busca el pago en la tabla
2. Haz clic en **Editar** (✏️)
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO EDITAR PAGO]
   ```
3. Modifica monto o método
4. Haz clic en **"Guardar Cambios"**

### Eliminar Pago

1. Busca el pago
2. Haz clic en **Eliminar** (🗑️)
3. Confirma la eliminación

---

## Gestión de Inventario

### Acceder al Módulo de Inventario

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO INVENTARIO]
```

**Ruta:** Menú Lateral → Inventario

### Vista de Inventario

Tabla con estado del stock:

| Columna | Descripción |
|---------|------------|
| **Producto** | Nombre del artículo |
| **Stock Actual** | Cantidad disponible |
| **Stock Mínimo** | Nivel de alerta |
| **Categoría** | Tipo de producto |
| **Última Actualización** | Cuándo se modificó |
| **Acciones** | Actualizar stock |

### Indicadores de Inventario

En la parte superior:

```
[ESPACIO PARA SCREENSHOT DE INDICADORES DE INVENTARIO]
```

- **Productos en Stock:** Cantidad disponible
- **Bajo Stock:** Productos bajo nivel mínimo
- **Sin Stock:** Productos agotados
- **Valor Total:** Valor del inventario en dinero

### Agregar Producto al Inventario

1. Haz clic en **"Agregar Producto"**
   ```
   [ESPACIO PARA SCREENSHOT DE FORMULARIO AGREGAR A INVENTARIO]
   ```

2. Selecciona el **Producto**

3. Ingresa:
   - **Cantidad:** Unidades a agregar
   - **Costo:** Precio de costo unitario
   - **Proveedor:** De dónde viene (opcional)
   - **Observaciones:** Notas adicionales

4. Haz clic en **"Guardar"**

### Actualizar Stock

1. Busca el producto en la tabla
2. Haz clic en **"Actualizar"** (o el ícono de edición)
   ```
   [ESPACIO PARA SCREENSHOT DE MODAL ACTUALIZAR STOCK]
   ```

3. Ingresa la **nueva cantidad**

4. Haz clic en **"Guardar"**

### Ajustar Stock por Merma o Pérdida

1. Selecciona el producto
2. Haz clic en **"Ajustar"**
3. Ingresa la cantidad a restar
4. Documenta el motivo (defectuoso, pérdida, etc.)
5. Guarda el ajuste

### Alertas de Inventario

El sistema avisa automáticamente cuando:

⚠️ **Stock bajo:** Producto por debajo del nivel mínimo  
❌ **Sin stock:** Producto agotado  
📦 **Nuevo ingreso:** Se agregó cantidad de productos

---

## Reportes y Análisis

### Acceder al Módulo de Reportes

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO REPORTES]
```

**Ruta:** Menú Lateral → Reportes

### Tipos de Reportes Disponibles

#### 1. Reporte de Ventas
```
[ESPACIO PARA SCREENSHOT DE REPORTE VENTAS]
```

Muestra:
- Total de ventas por período
- Cantidad de transacciones
- Producto más vendido
- Cliente más frecuente
- Gráficos de tendencias

#### 2. Reporte de Ingresos
```
[ESPACIO PARA SCREENSHOT DE REPORTE INGRESOS]
```

Incluye:
- Dinero total recibido
- Desglose por método de pago
- Comparativa con períodos anteriores
- Proyecciones

#### 3. Reporte de Inventario
```
[ESPACIO PARA SCREENSHOT DE REPORTE INVENTARIO]
```

Contenido:
- Productos en stock
- Nivel de inventario
- Valor total del stock
- Movimientos de entrada/salida
- Productos sin movimiento

#### 4. Análisis de Clientes
```
[ESPACIO PARA SCREENSHOT DE ANÁLISIS CLIENTES]
```

Datos:
- Total de clientes registrados
- Cliente top (mayor comprador)
- Frecuencia de compra
- Valor promedio de compra
- Historial de compras

#### 5. Análisis de Productos
```
[ESPACIO PARA SCREENSHOT DE ANÁLISIS PRODUCTOS]
```

Información:
- Producto más vendido
- Producto menos vendido
- Rentabilidad por producto
- Categorías más vendidas
- Análisis de márgenes

### Generar Reporte

1. Selecciona el tipo de reporte

2. Configura los **Filtros:**
   - **Período:** Hoy, Última Semana, Último Mes, Personalizado
   - **Rango de Fechas:** Selecciona inicio y fin

3. Haz clic en **"Generar"**
   ```
   [ESPACIO PARA SCREENSHOT DE REPORTE GENERADO]
   ```

4. Visualiza o **Descarga:**
   - Botón **"Descargar PDF"**
   - Botón **"Descargar Excel"**
   - Botón **"Imprimir"**

### Interpretar Gráficos

Los reportes incluyen diferentes tipos de gráficos:

- **Gráfico de Líneas:** Tendencias a lo largo del tiempo
- **Gráfico de Barras:** Comparación entre categorías
- **Gráfico Circular:** Proporción del total
- **Tabla de Datos:** Detalles numéricos

---

## Configuración del Sistema

### Acceder a Configuración

```
[ESPACIO PARA SCREENSHOT DEL MÓDULO CONFIGURACIÓN]
```

**Ruta:** Menú Lateral → Configuración

### Opciones de Configuración General

#### 1. Información de la Empresa
```
[ESPACIO PARA SCREENSHOT DE INFORMACIÓN EMPRESA]
```

Campos editables:
- Nombre de la empresa
- Dirección principal
- Teléfono de contacto
- Email de contacto
- Logo de la empresa
- Datos fiscales

#### 2. Configuración de Notificaciones
```
[ESPACIO PARA SCREENSHOT DE NOTIFICACIONES]
```

Activa/Desactiva:
- Alertas de bajo stock
- Confirmación de ventas
- Alertas de pagos recibidos
- Reportes automáticos
- Notificaciones por email

#### 3. Configuración de Seguridad
```
[ESPACIO PARA SCREENSHOT DE SEGURIDAD]
```

Opciones de seguridad:
- Cambiar contraseña personal
- Autenticación de doble factor
- Sesiones activas
- Historial de accesos
- Política de contraseñas

#### 4. Backup y Restauración
```
[ESPACIO PARA SCREENSHOT DE BACKUP]
```

Acciones disponibles:
- **Realizar Backup:** Descarga copia de seguridad
- **Programar Backup Automático:** Define frecuencia
- **Restaurar Backup:** Recupera datos anteriores
- **Ver Historial:** Backups realizados

### Realizar Cambios

1. Accede a la sección que deseas modificar
2. Edita los campos necesarios
3. Haz clic en **"Guardar Cambios"**
4. Verás confirmación de los cambios guardados

---

## Preguntas Frecuentes

### General

**P: ¿Cómo accedo al sistema?**  
R: Ve a `http://127.0.0.1:5000/` e ingresa tu usuario y contraseña. Si no tienes acceso, contacta al administrador.

**P: ¿Qué hago si olvido mi contraseña?**  
R: Contacta al administrador del sistema para que reinicie tu contraseña.

**P: ¿En qué horario puedo usar el sistema?**  
R: El sistema está disponible 24/7. Si hay mantenimiento programado, se notificará con anticipación.

### Usuarios

**P: ¿Puedo cambiar mi contraseña?**  
R: Sí, ve a Configuración → Mi Perfil → Cambiar Contraseña.

**P: ¿Cuántos usuarios activos puede tener el sistema?**  
R: No hay límite técnico, pero depende de tu licencia. Consulta con el administrador.

**P: ¿Qué roles existen en el sistema?**  
R: Administrador, Vendedor, Almacenero, Reportes. Tu rol determina qué puedes hacer.

### Productos

**P: ¿Cómo agrego múltiples productos a la vez?**  
R: Actualmente se agregan uno por uno. En futuras versiones habrá importación masiva.

**P: ¿Puedo cambiar el precio de un producto después de venderlo?**  
R: Sí, pero solo afectará futuras ventas. Las ventas realizadas mantienen su precio original.

**P: ¿Cómo sé si un producto tiene bajo stock?**  
R: El sistema muestra una alerta cuando el stock cae bajo el nivel mínimo configurado.

### Ventas

**P: ¿Puedo eliminar una venta registrada?**  
R: El administrador puede eliminarla, pero se recomienda crear una nota de crédito.

**P: ¿Puedo hacer devoluciones?**  
R: Sí, registra un pago negativo o crea una nota de crédito en el sistema.

**P: ¿Puedo aplicar descuentos?**  
R: Sí, durante el proceso de venta hay campo para descuentos.

### Pagos

**P: ¿Qué métodos de pago soporta?**  
R: Efectivo, Tarjeta de Crédito, Tarjeta de Débito, Transferencia Bancaria.

**P: ¿Puedo registrar un pago parcial?**  
R: Sí, registra el monto recibido y deja la diferencia pendiente.

**P: ¿Dónde veo el dinero recibido hoy?**  
R: En la pantalla de Pagos hay indicadores que muestran totales en tiempo real.

### Reportes

**P: ¿Puedo exportar los reportes?**  
R: Sí, en formato PDF o Excel desde la pantalla del reporte.

**P: ¿Con qué frecuencia se actualizan los datos?**  
R: Los datos son en tiempo real. Cualquier cambio se refleja inmediatamente.

**P: ¿Cuánto tiempo se guardan los datos históricos?**  
R: Todo el historial se mantiene indefinidamente a menos que se ejecute un borrado manual.

---

## Información de Contacto y Soporte

### Soporte Técnico

**Email:** soporte@ecomdata.com  
**Teléfono:** +XX (XXX) XXXX-XXXX  
**WhatsApp:** +XX (XXX) XXXX-XXXX  
**Horario de Atención:** Lunes a Viernes 9:00 - 18:00 hrs

### Reportar Problemas

1. Describe el problema con detalle
2. Incluye si es posible:
   - Screenshots del error
   - Pasos para reproducirlo
   - Nombre de usuario
   - Navegador utilizado
   - Versión del sistema

3. Envía por email al equipo de soporte

### Centro de Ayuda En Línea

Visita nuestra base de conocimientos:
```
[URL DEL CENTRO DE AYUDA]
```

Encontrarás:
- Tutoriales en video
- Guías paso a paso
- Preguntas frecuentes
- Notas de actualización

### Reporte de Bugs

¿Encontraste un error? Repórtalo:

**Información a incluir:**
- Descripción del problema
- Pasos para reproducir
- Navegador y versión
- Datos del error (si los hay)
- Screenshots si es posible

---

## Consejos y Buenas Prácticas

### Para Mejorar tu Productividad

1. **Aprende los Atajos de Teclado**
   - Tab: Mover entre campos
   - Enter: Enviar formulario
   - Esc: Cerrar modal/diálogo

2. **Usa Filtros Efectivamente**
   - Ahorra tiempo buscando por criterios específicos

3. **Mantén Datos Actualizados**
   - Ingresa información correctamente desde el inicio

4. **Realiza Backups Regularmente**
   - No confíes solo en el backup automático

5. **Revisa Reportes Periódicamente**
   - Ayuda a tomar mejores decisiones

### Para Mantener la Seguridad

1. **Cambia tu Contraseña Regularmente**
   - Cada 3 meses es recomendable

2. **No Compartas tu Acceso**
   - Cada usuario debe tener su propia cuenta

3. **Cierra Sesión Siempre**
   - Especialmente en equipos compartidos

4. **Usa Conexión Segura**
   - En redes públicas usa VPN

5. **Reporta Accesos Sospechosos**
   - Contacta al administrador inmediatamente

---

## Actualizaciones y Cambios

### Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|-------------------|
| 1.0.0 | Nov 2025 | Lanzamiento inicial |
| | | |
| | | |

### Próximas Características Planeadas

- [ ] Importación masiva de productos
- [ ] Descuentos automáticos por volumen
- [ ] Integración con sistemas de pago online
- [ ] App móvil
- [ ] Notificaciones por SMS
- [ ] Control de devoluciones
- [ ] Sucursales múltiples

---

## Apéndice: Atajos y Referencias Rápidas

### URLs Directas a Módulos

| Módulo | URL |
|--------|-----|
| Inicio | `/inicio` |
| Usuarios | `/usuarios` |
| Productos | `/catalogo_productos` |
| Clientes | `/clientes` |
| Ventas | `/ventas` |
| Pagos | `/pagos` |
| Inventario | `/inventario` |
| Reportes | `/reportes` |
| Configuración | `/configuracion_general` |

### Símbolos y Significados

| Símbolo | Significado | Acción |
|---------|------------|--------|
| ✏️ | Editar | Modifica el registro |
| 🗑️ | Eliminar | Borra el registro |
| 👁️ | Ver | Muestra detalles |
| 💾 | Guardar | Almacena cambios |
| ❌ | Cancelar | Descarta cambios |
| ✓ | Confirmar | Valida acciones |
| ⚙️ | Configuración | Ajustes |
| 🔍 | Buscar | Localiza registros |

---

## Términos Importantes

- **Venta:** Transacción de productos con un cliente
- **Pago:** Dinero recibido por una venta
- **Inventario:** Stock de productos disponibles
- **SKU:** Código único del producto
- **Rol:** Función o permiso del usuario
- **Backup:** Copia de seguridad de datos
- **Backend:** Sistema detrás del navegador
- **Módulo:** Sección funcional del sistema

---

## Notas Finales

Este manual proporciona orientación general sobre el uso del sistema EcomData. Para consultas específicas o problemas técnicos, no dudes en contactar al equipo de soporte.

**Agradecemos tu uso de EcomData y esperamos que sea útil para tu negocio.**

---

**Manual de Usuario - EcomData v1.0.0**  
**Última Actualización:** Noviembre 2025  
**Próxima Revisión:** Diciembre 2025

*Este documento es confidencial y está destinado solo para usuarios autorizados del sistema EcomData.*
