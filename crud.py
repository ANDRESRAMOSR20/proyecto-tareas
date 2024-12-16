from sqlalchemy.orm import Session
from database import Tarea

# Crear una nueva tarea
def crear_tarea(db: Session, titulo: str, descripcion: str):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

# Obtener todas las tareas
def obtener_tareas(db: Session):
    return db.query(Tarea).all()

# Marcar una tarea como completada
def completar_tarea(db: Session, tarea_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        tarea.completada = True
        db.commit()
    return tarea

# Eliminar una tarea
def eliminar_tarea(db: Session, tarea_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        db.delete(tarea)
        db.commit()
