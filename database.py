# database.py
from sqlmodel import create_engine, SQLModel, Session
import os

# --- URL de Conexión a la Base de Datos ---
# Formato: postgresql://USUARIO:CONTRASEÑA@HOST_DE_RDS:PUERTO/NOMBRE_DB
# Para seguridad, es una mala práctica escribir las credenciales aquí.
# Las leeremos de variables de entorno (que configuraremos luego en el servidor).
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_PORT = os.getenv("DB_PORT", "5432")

# Construimos la URL de conexión
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Creamos el "motor" de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Función para crear las tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Función para obtener una sesión (una conversación con la DB)
def get_session():
    with Session(engine) as session:
        yield session