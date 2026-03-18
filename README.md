# API de Gestión de Tareas con Flask

API REST para gestionar una lista de tareas con operaciones CRUD (Create, Read, Update, Delete).

## Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Ejecutar la aplicación:**
```bash
python app.py
```

La API estará disponible en: `http://localhost:5000`

---

## Endpoints

### 1. **GET `/tareas`** - Obtener todas las tareas
Obtiene la lista completa de todas las tareas.

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "titulo": "Comprar leche",
    "descripcion": "En el supermercado",
    "completada": false,
    "fecha_creacion": "2026-03-17 10:30:00",
    "fecha_actualizacion": "2026-03-17 10:30:00"
  }
]
```

---

### 2. **GET `/tareas/<id>`** - Obtener una tarea específica
Obtiene los detalles de una tarea por su ID.

**Parámetros:**
- `id` (integer): ID de la tarea

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar leche",
  "descripcion": "En el supermercado",
  "completada": false,
  "fecha_creacion": "2026-03-17 10:30:00",
  "fecha_actualizacion": "2026-03-17 10:30:00"
}
```

**Error (404 Not Found):**
```json
{
  "error": "Tarea no encontrada"
}
```

---

### 3. **POST `/tareas`** - Crear una nueva tarea
Crea una nueva tarea en la lista.

**Body (JSON):**
```json
{
  "titulo": "Comprar leche",
  "descripcion": "En el supermercado",
  "completada": false
}
```

**Campos:**
- `titulo` (string, **requerido**): Título de la tarea
- `descripcion` (string, opcional): Descripción detallada
- `completada` (boolean, opcional): Estado de la tarea (default: false)

**Respuesta (201 Created):**
```json
{
  "id": 1,
  "titulo": "Comprar leche",
  "descripcion": "En el supermercado",
  "completada": false,
  "fecha_creacion": "2026-03-17 10:30:00",
  "fecha_actualizacion": "2026-03-17 10:30:00"
}
```

**Error (400 Bad Request):**
```json
{
  "error": "El título es requerido"
}
```

---

### 4. **PUT `/tareas/<id>`** - Actualizar una tarea
Actualiza los datos de una tarea existente.

**Parámetros:**
- `id` (integer): ID de la tarea a actualizar

**Body (JSON):**
```json
{
  "titulo": "Comprar leche y pan",
  "descripcion": "En el supermercado cerca de casa",
  "completada": true
}
```

**Campos actualizables:**
- `titulo` (string, opcional)
- `descripcion` (string, opcional)
- `completada` (boolean, opcional)

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "titulo": "Comprar leche y pan",
  "descripcion": "En el supermercado cerca de casa",
  "completada": true,
  "fecha_creacion": "2026-03-17 10:30:00",
  "fecha_actualizacion": "2026-03-17 11:00:00"
}
```

**Error (404 Not Found):**
```json
{
  "error": "Tarea no encontrada"
}
```

---

### 5. **DELETE `/tareas/<id>`** - Eliminar una tarea
Elimina una tarea específica por su ID.

**Parámetros:**
- `id` (integer): ID de la tarea a eliminar

**Respuesta (200 OK):**
```json
{
  "mensaje": "Tarea eliminada correctamente"
}
```

**Error (404 Not Found):**
```json
{
  "error": "Tarea no encontrada"
}
```

---

### 6. **DELETE `/tareas`** - Eliminar todas las tareas
Elimina todas las tareas de la lista.

**Respuesta (200 OK):**
```json
{
  "mensaje": "Todas las tareas han sido eliminadas"
}
```

---

## Ejemplos de Uso

### Con cURL

```bash
# Crear una tarea
curl -X POST http://localhost:5000/tareas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Comprar leche", "descripcion": "Supermercado"}'

# Obtener todas las tareas
curl http://localhost:5000/tareas

# Obtener una tarea específica
curl http://localhost:5000/tareas/1

# Actualizar una tarea
curl -X PUT http://localhost:5000/tareas/1 \
  -H "Content-Type: application/json" \
  -d '{"completada": true}'

# Eliminar una tarea
curl -X DELETE http://localhost:5000/tareas/1

# Eliminar todas las tareas
curl -X DELETE http://localhost:5000/tareas
```

### Con Python

Ver el archivo `ejemplos_uso.py` para ejemplos completos en Python.

---

## Códigos de Estado HTTP

| Código | Descripción |
|--------|-------------|
| 200 | OK - Operación exitosa |
| 201 | Created - Recurso creado |
| 400 | Bad Request - Datos inválidos |
| 404 | Not Found - Recurso no encontrado |
| 500 | Internal Server Error - Error del servidor |

---

## Estructura de Datos

Una tarea tiene la siguiente estructura:

```json
{
  "id": 1,
  "titulo": "string",
  "descripcion": "string",
  "completada": "boolean",
  "fecha_creacion": "datetime",
  "fecha_actualizacion": "datetime"
}
```

---

## Notas

- La API almacena las tareas en memoria (se pierden al reiniciar)
- Los IDs se asignan automáticamente de forma secuencial
- Las fechas se registran automáticamente al crear y actualizar
- La API está configurada para aceptar requests desde cualquier host (0.0.0.0)

---

## Mejoras Futuras

- Añadir persistencia con base de datos (SQLite, PostgreSQL)
- Autenticación y autorización
- Paginación de resultados
- Filtrado y búsqueda avanzada
- Categorías y etiquetas para tareas
- Prioridades y fechas de vencimiento
