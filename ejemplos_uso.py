"""
Exemplos de uso de la API de Tareas

Para probar los endpoints, puede usar curl:
"""

# EJEMPLOS CON CURL

# 1. GET - Obtener todas las tareas
# curl http://localhost:5000/tareas

# 2. POST - Crear una nueva tarea
# curl -X POST http://localhost:5000/tareas \
#   -H "Content-Type: application/json" \
#   -d '{"titulo": "Comprar leche", "descripcion": "Ir al supermercado"}'

# 3. GET - Obtener una tarea específica (ID 1)
# curl http://localhost:5000/tareas/1

# 4. PUT - Actualizar una tarea
# curl -X PUT http://localhost:5000/tareas/1 \
#   -H "Content-Type: application/json" \
#   -d '{"titulo": "Comprar leche y pan", "completada": true}'

# 5. DELETE - Eliminar una tarea
# curl -X DELETE http://localhost:5000/tareas/1

# 6. DELETE - Eliminar todas las tareas
# curl -X DELETE http://localhost:5000/tareas


# EJEMPLOS CON PYTHON

import requests
import json

BASE_URL = "http://localhost:5000"

# 1. Obtener todas las tareas
def obtener_todas_tareas():
    response = requests.get(f"{BASE_URL}/tareas")
    print(json.dumps(response.json(), indent=2))

# 2. Crear una tarea
def crear_tarea(titulo, descripcion=""):
    datos = {
        "titulo": titulo,
        "descripcion": descripcion
    }
    response = requests.post(f"{BASE_URL}/tareas", json=datos)
    print(json.dumps(response.json(), indent=2))

# 3. Obtener una tarea por ID
def obtener_tarea(tarea_id):
    response = requests.get(f"{BASE_URL}/tareas/{tarea_id}")
    print(json.dumps(response.json(), indent=2))

# 4. Actualizar una tarea
def actualizar_tarea(tarea_id, titulo=None, descripcion=None, completada=None):
    datos = {}
    if titulo:
        datos["titulo"] = titulo
    if descripcion:
        datos["descripcion"] = descripcion
    if completada is not None:
        datos["completada"] = completada
    response = requests.put(f"{BASE_URL}/tareas/{tarea_id}", json=datos)
    print(json.dumps(response.json(), indent=2))

# 5. Eliminar una tarea
def eliminar_tarea(tarea_id):
    response = requests.delete(f"{BASE_URL}/tareas/{tarea_id}")
    print(json.dumps(response.json(), indent=2))

# 6. Eliminar todas las tareas
def eliminar_todas():
    response = requests.delete(f"{BASE_URL}/tareas")
    print(json.dumps(response.json(), indent=2))


# Ejecutar ejemplo
if __name__ == "__main__":
    print("=== Ejemplo 1: Crear 3 tareas ===")
    crear_tarea("Comprar leche", "En el supermercado")
    crear_tarea("Limpiar la casa", "Limpiar todas las habitaciones")
    crear_tarea("Estudiar Flask", "Aprender API REST")
    
    print("\n=== Ejemplo 2: Obtener todas las tareas ===")
    obtener_todas_tareas()
    
    print("\n=== Ejemplo 3: Obtener una tarea específica ===")
    obtener_tarea(1)
    
    print("\n=== Ejemplo 4: Actualizar una tarea ===")
    actualizar_tarea(1, "Comprar leche y pan", completada=True)
    
    print("\n=== Ejemplo 5: Eliminar una tarea ===")
    eliminar_tarea(2)
    
    print("\n=== Ejemplo 6: Obtener todas las tareas (después de eliminar) ===")
    obtener_todas_tareas()
