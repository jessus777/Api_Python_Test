from pydantic import BaseModel


class SolicitudUpdate(BaseModel):
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: str
    estatus: str