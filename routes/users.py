from fastapi import APIRouter, HTTPException
from typing import List
from sqlmodel import select
from models import Usuario
from db import SessionDep

# 'APIRouter' es como una mini-aplicación FastAPI.
# Nos permite agrupar todas las rutas relacionadas con usuarios.
router = APIRouter(
    prefix="/usuarios",  # Todas las rutas aquí empezarán con /usuarios
    tags=["usuarios"],   # Etiqueta para la documentación
)

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: SessionDep):
    """Crea un nuevo usuario en la base de datos."""
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.get("/", response_model=List[Usuario])
def listar_usuarios(session: SessionDep):
    """Obtiene una lista de todos los usuarios."""
    usuarios = session.exec(select(Usuario)).all()
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int, session: SessionDep):
    """Obtiene un usuario específico por su ID."""
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, datos: Usuario, session: SessionDep):
    """Actualiza la información de un usuario."""
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuario.nombre = datos.nombre
    usuario.email = datos.email
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, session: SessionDep):
    """Elimina un usuario de la base de datos."""
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    session.delete(usuario)
    session.commit()
    return {"ok": True, "mensaje": "Usuario eliminado correctamente"}
