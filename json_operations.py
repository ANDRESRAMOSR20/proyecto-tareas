import json
from os import path

TASKS_FILE = "tareas.json"

# Función para cargar tareas desde el archivo JSON
def cargar_tareas():
    if path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:  # Capturar el error si el archivo está vacío
                return []  # Si el archivo está vacío, retornar una lista vacía
    return []  # Si el archivo no existe, retornar una lista vacía

# Función para guardar tareas en el archivo JSON
def guardar_tareas(tareas):
    with open(TASKS_FILE, "w") as file:
        json.dump(tareas, file, indent=4)
