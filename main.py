from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Estudiante(BaseModel):
    id: int
    nombre: str
    edad: int

# Base de datos simulada
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
    Devuelve todos los estudiantes en la base de datos simulada.
    """
    return db_estudiantes


@app.get("/estudiantes/{estudiante_id}", response_model=Estudiante)
def get_estudiante_por_id(estudiante_id: int):
    """
    Devuelve un estudiante por su ID.
    """
    for estudiante in db_estudiantes:
        if estudiante.id == estudiante_id:
            return estudiante
    
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")


@app.put("/estudiantes/{estudiante_id}", response_model=Estudiante)
def update_estudiante(estudiante_id: int, estudiante_actualizado: Estudiante):
    """
    Actualiza los datos de un estudiante por su ID.
    """
    for i, estudiante in enumerate(db_estudiantes):
        if estudiante.id == estudiante_id:
            db_estudiantes[i] = estudiante_actualizado
            return estudiante_actualizado
    
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")


@app.delete("/estudiantes/{estudiante_id}", response_model=Estudiante)
def delete_estudiante(estudiante_id: int):
    """
    Elimina un estudiante de la base de datos por su ID.
    """
    for estudiante in db_estudiantes:
        if estudiante.id == estudiante_id:
            db_estudiantes.remove(estudiante)
            return estudiante
    
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
