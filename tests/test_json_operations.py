import os
import pytest
from json_operations import cargar_tareas, guardar_tareas

# Ruta al archivo de tareas JSON
TASKS_FILE = "tareas.json"


# Limpiar el archivo JSON antes de cada prueba
@pytest.fixture(autouse=True)
def limpiar_archivo_json():
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)


# Prueba para verificar la carga de tareas
def test_cargar_tareas_vacias():
    tareas = cargar_tareas()
    assert tareas == [], "Las tareas deben estar vacías si el archivo no existe o está vacío"


# Prueba para verificar la carga de tareas cuando el archivo tiene datos
def test_cargar_tareas_con_datos():
    tareas_test = [{"titulo": "Tarea 1", "descripcion": "Descripción 1", "completada": False}]
    guardar_tareas(tareas_test)

    tareas = cargar_tareas()
    assert len(tareas) == 1, "Debe cargar una tarea"
    assert tareas[0]["titulo"] == "Tarea 1", "El título de la tarea debe ser 'Tarea 1'"


# Prueba para verificar la función guardar_tareas
def test_guardar_tareas():
    tareas_test = [{"titulo": "Tarea 1", "descripcion": "Descripción 1", "completada": False}]
    guardar_tareas(tareas_test)

    tareas = cargar_tareas()
    assert len(tareas) == 1, "Debe guardar correctamente la tarea"
    assert tareas[0]["titulo"] == "Tarea 1", "El título de la tarea guardada debe ser 'Tarea 1'"
