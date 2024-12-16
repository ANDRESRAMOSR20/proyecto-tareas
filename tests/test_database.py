import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from database import Base, Tarea, init_db

DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture
def db_engine():
    """Fixture para crear el motor de base de datos de prueba."""
    engine = create_engine(DATABASE_URL)
    yield engine
    engine.dispose()

@pytest.fixture
def db_session(db_engine):
    """Fixture para inicializar las tablas y proporcionar una sesión."""
    init_db(db_engine)  # Usar el motor en memoria
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=db_engine)

def test_init_db(db_engine):
    """Prueba para verificar que init_db crea las tablas correctamente."""
    Base.metadata.drop_all(bind=db_engine)  # Limpiar tablas previas
    init_db(db_engine)  # Pasar el motor en memoria

    # Usar el inspector para verificar las tablas
    inspector = inspect(db_engine)
    tables = inspector.get_table_names()
    assert "tareas" in tables

def test_tarea_model(db_session):
    """Prueba para verificar el modelo Tarea."""
    nueva_tarea = Tarea(titulo="Test Tarea", descripcion="Descripción de prueba", completada=False)
    db_session.add(nueva_tarea)
    db_session.commit()
    db_session.refresh(nueva_tarea)

    assert nueva_tarea.id is not None
    assert nueva_tarea.titulo == "Test Tarea"
    assert nueva_tarea.descripcion == "Descripción de prueba"
    assert nueva_tarea.completada is False
