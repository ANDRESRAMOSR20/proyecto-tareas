import streamlit as st
from os import path
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import crear_tarea, obtener_tareas, completar_tarea, eliminar_tarea
from json_operations import cargar_tareas, guardar_tareas


# Agregar tarea al archivo JSON y la base de datos
def agregar_tarea(db, titulo, descripcion):
    tarea_nueva = {"titulo": titulo, "descripcion": descripcion, "completada": False}
    crear_tarea(db, titulo, descripcion)  # Agrega la tarea a la base de datos

    tareas = cargar_tareas()
    tarea_nueva['id'] = len(tareas) + 1
    tareas.append(tarea_nueva)
    guardar_tareas(tareas)


# Completar tarea (en base de datos y archivo JSON)
def completar_tarea_action(db, tareas, index):
    completar_tarea(db, tareas[index]['id'])
    tareas[index]['completada'] = True
    guardar_tareas(tareas)
    st.rerun()


# Eliminar tarea (en base de datos y archivo JSON)
def eliminar_tarea_action(db, tareas, index):
    eliminar_tarea(db, tareas[index]['id'])
    tareas.pop(index)
    guardar_tareas(tareas)
    st.rerun()


# Función principal de la aplicación
def main():
    st.title("Gestión de Tareas con Python")

    menu = ["Agregar Tarea", "Ver Tareas"]
    choice = st.sidebar.selectbox("Menú", menu)

    db = SessionLocal()
    tareas = cargar_tareas()

    if choice == "Agregar Tarea":
        agregar_tarea_ui(db)

    elif choice == "Ver Tareas":
        ver_tareas_ui(tareas, db)


def agregar_tarea_ui(db):
    st.subheader("Agregar Nueva Tarea")
    titulo = st.text_input("Título de la tarea")
    descripcion = st.text_area("Descripción de la tarea")
    if st.button("Agregar"):
        if titulo:
            agregar_tarea(db, titulo, descripcion)
            st.success(f"Tarea '{titulo}' agregada con éxito.")
        else:
            st.error("El título es obligatorio.")


def ver_tareas_ui(tareas, db):
    st.subheader("Lista de Tareas")
    if not tareas:
        st.write("No hay tareas.")
    else:
        for index, tarea in enumerate(tareas):
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.write(f"📌 **{tarea['titulo']}** - {tarea['descripcion']}")
            col2.write("✔️ Completada" if tarea["completada"] else "⏳ Pendiente")

            if not tarea["completada"] and col3.button("Completar", key=f"comp_{index}"):
                completar_tarea_action(db, tareas, index)

            if col3.button("Eliminar", key=f"del_{index}"):
                eliminar_tarea_action(db, tareas, index)


if __name__ == "__main__":
    main()
