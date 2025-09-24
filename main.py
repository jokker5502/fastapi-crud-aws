# main.py
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select
from database import get_session, create_db_and_tables
from models import Cliente, Factura

app = FastAPI(title="API con RDS")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Endpoints para Clientes
@app.post("/clientes/", response_model=Cliente)
def create_cliente(cliente: Cliente, session = Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@app.get("/clientes/", response_model=List[Cliente])
def read_clientes(session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    return clientes

# (Puedes añadir los demás endpoints de CRUD aquí: GET por ID, PUT, DELETE)