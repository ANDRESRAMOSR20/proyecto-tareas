from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Crear el motor de la base de datos SQLite
DATABASE_URL = "sqlite:///tareas.db"  # Crea el archivo tareas.db en el mismo directorio
engine = create_engine(DATABASE_URL)

# Declaración base para los modelos
Base = declarative_base()

# Definición del modelo de tabla
class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para inicializar la base de datos
def init_db(custom_engine=None):
    """Inicializa la base de datos con el motor proporcionado."""
    engine_to_use = custom_engine if custom_engine else engine
    Base.metadata.create_all(bind=engine_to_use)
