# models.py
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
import datetime

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    email: str = Field(unique=True)
    fecha_registro: datetime.date
    facturas: List["Factura"] = Relationship(back_populates="cliente")

class Factura(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    monto: float
    fecha_emision: datetime.date
    cliente_id: int = Field(foreign_key="cliente.id")
    cliente: Cliente = Relationship(back_populates="facturas")