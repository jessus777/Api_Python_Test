from pydantic import BaseModel


class SolicitudCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int
    afinidad_magica: str