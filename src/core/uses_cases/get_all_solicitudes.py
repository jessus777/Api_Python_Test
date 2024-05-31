from typing import List
from src.core.entities.solicitud import Solicitud
from src.core.Interfaces.solicitu_repository import SolicitudRepository

class GetAllSolicitudes:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    def execute(self) -> List[Solicitud]:
        return self.solicitud_repository.get_all()