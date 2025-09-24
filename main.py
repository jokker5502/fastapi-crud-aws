from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_all_tables
from routes import users  

# El 'lifespan' es la forma moderna de manejar eventos de inicio y apagado.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando aplicación...")
    # Llamamos a la función para crear tablas (sin el yield)
    # Nota: El 'yield' está dentro de la función original en db.py
    create_all_tables(app).__next__() 
    yield
    print("Apagando aplicación...")

app = FastAPI(
    title="API con RDS y Rutas Modulares",
    description="Laboratorio con base de datos en AWS RDS.",
    lifespan=lifespan
)

# Aquí "incluimos" todas las rutas que definimos en el archivo routes/users.py
# en nuestra aplicación principal.
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API"}
