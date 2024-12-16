import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database import Base, Tarea  # Importa el modelo de la base de datos
from crud import crear_tarea, obtener_tareas, completar_tarea, eliminar_tarea

# Crear un motor en memoria para SQLite
DATABASE_URL = "sqlite:///:memory:"


# Configurar la base de datos de prueba y crear tablas
@pytest.fixture
def db_session():
    engine = create_engine(DATABASE_URL)
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Crear las tablas en la base de datos de prueba
    Base.metadata.create_all(bind=engine)

    # Proporcionar la sesión para las pruebas
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Eliminar tablas después de la prueba


# Prueba para `crear_tarea`
def test_crear_tarea(db_session: Session):
    tarea = crear_tarea(db_session, titulo="Prueba Tarea", descripcion="Descripción de prueba")
    assert tarea.id is not None
    assert tarea.titulo == "Prueba Tarea"
    assert tarea.descripcion == "Descripción de prueba"
    assert not tarea.completada


# Prueba para `obtener_tareas`
def test_obtener_tareas(db_session: Session):
    # Crear datos de prueba
    crear_tarea(db_session, "Tarea 1", "Descripción 1")
    crear_tarea(db_session, "Tarea 2", "Descripción 2")

    tareas = obtener_tareas(db_session)
    assert len(tareas) == 2
    assert tareas[0].titulo == "Tarea 1"
    assert tareas[1].titulo == "Tarea 2"


# Prueba para `completar_tarea`
def test_completar_tarea(db_session: Session):
    tarea = crear_tarea(db_session, "Tarea Completar", "Descripción")
    completar_tarea(db_session, tarea.id)

    tarea_actualizada = db_session.query(Tarea).filter(Tarea.id == tarea.id).first()
    assert tarea_actualizada.completada


# Prueba para `eliminar_tarea`
def test_eliminar_tarea(db_session: Session):
    tarea = crear_tarea(db_session, "Tarea Eliminar", "Descripción")
    eliminar_tarea(db_session, tarea.id)

    tarea_borrada = db_session.query(Tarea).filter(Tarea.id == tarea.id).first()
    assert tarea_borrada is None
