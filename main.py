from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Estudiante(BaseModel):
    id: int
    nombre: str
    edad: int


db_estudiantes = [
    Estudiante(id=1, nombre="Ana Gómez", edad=21),
    Estudiante(id=2, nombre="Carlos Ruiz", edad=23),
    Estudiante(id=3, nombre="Sofía Luna", edad=20),
]

app = FastAPI(
    title="API de Estudiantes",
    description="Una API súper simple para gestionar estudiantes."
)


@app.get("/estudiantes/", response_model=List[Estudiante])
def get_todos_los_estudiantes():
    """
    Esta función se ejecuta cuando alguien visita /estudiantes/
    y simplemente devuelve la lista completa de 'db_estudiantes'.
    """
    return db_estudiantes


@app.get("/estudiantes/{estudiante_id}", response_model=Estudiante)
def get_estudiante_por_id(estudiante_id: int):
    """
    Esta función se ejecuta cuando alguien visita /estudiantes/1, /estudiantes/2, etc.
    Busca en la lista 'db_estudiantes' al estudiante que tenga el ID correcto.
    """
    for estudiante in db_estudiantes:
        if estudiante.id == estudiante_id:
            return estudiante
    
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")


@app.delete("/estudiantes/{estudiante_id}", response_model=Estudiante)
def delete_estudiante(estudiante_id: int):
    """
    Esta función se ejecuta cuando alguien visita /estudiantes/{id} con el método DELETE.
    Elimina al estudiante con el ID proporcionado de la lista 'db_estudiantes'.
    """
    for estudiante in db_estudiantes:
        if estudiante.id == estudiante_id:
            db_estudiantes.remove(estudiante)
            return estudiante
    
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
