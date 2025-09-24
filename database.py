from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# --- URL de Conexión a la Base de Datos ---
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "uide.asu.123")
DB_HOST = os.getenv("DB_HOST", "mi-api-database.c07yeca6uwgy.us-east-1.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Creamos el "motor" de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# --- Funciones y Dependencias ---

def get_session():
    """Generador de sesión para la base de datos."""
    with Session(engine) as session:
        yield session

# Esta es la forma moderna de declarar una dependencia en FastAPI.
# Es lo que tu profesor usó como 'SessionDep'.
SessionDep = Annotated[Session, Depends(get_session)]

def create_all_tables(app):
    """
    Función que se ejecuta al iniciar la aplicación para crear las tablas.
    El profesor usa 'lifespan' en el main.py para llamarla.
    """
    print("Creando tablas...")
    SQLModel.metadata.create_all(engine)
    print("Tablas creadas.")
    yield
