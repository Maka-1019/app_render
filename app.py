from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Base de datos simulada (lista de tareas)
tareas = []
id_counter = 1


# GET - Obtener todas las tareas
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    """Obtiene la lista completa de tareas"""
    return jsonify(tareas), 200


# GET - Obtener una tarea por ID
@app.route('/tareas/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    """Obtiene una tarea específica por su ID"""
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    if tarea:
        return jsonify(tarea), 200
    return jsonify({'error': 'Tarea no encontrada'}), 404


# POST - Crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    """Crea una nueva tarea"""
    global id_counter
    
    datos = request.get_json()
    
    # Validar que el título esté presente
    if not datos or 'titulo' not in datos:
        return jsonify({'error': 'El título es requerido'}), 400
    
    nueva_tarea = {
        'id': id_counter,
        'titulo': datos['titulo'],
        'descripcion': datos.get('descripcion', ''),
        'completada': datos.get('completada', False),
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'fecha_actualizacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    tareas.append(nueva_tarea)
    id_counter += 1
    
    return jsonify(nueva_tarea), 201


# PUT - Actualizar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    """Actualiza una tarea existente"""
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    datos = request.get_json()
    
    # Actualizar los campos proporcionados
    if 'titulo' in datos:
        tarea['titulo'] = datos['titulo']
    if 'descripcion' in datos:
        tarea['descripcion'] = datos['descripcion']
    if 'completada' in datos:
        tarea['completada'] = datos['completada']
    
    tarea['fecha_actualizacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return jsonify(tarea), 200


# DELETE - Eliminar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    """Elimina una tarea"""
    global tareas
    
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    tareas = [t for t in tareas if t['id'] != tarea_id]
    
    return jsonify({'mensaje': 'Tarea eliminada correctamente'}), 200


# DELETE - Eliminar todas las tareas
@app.route('/tareas', methods=['DELETE'])
def eliminar_todas_tareas():
    """Elimina todas las tareas"""
    global tareas
    tareas = []
    return jsonify({'mensaje': 'Todas las tareas han sido eliminadas'}), 200


# Manejo de errores
@app.errorhandler(404)
def no_encontrado(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404


@app.errorhandler(500)
def error_servidor(error):
    return jsonify({'error': 'Error interno del servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
