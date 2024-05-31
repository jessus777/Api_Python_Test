from typing import List
from src.core.entities.grimoire import Grimoire
from src.core.Interfaces.solicitu_repository import SolicitudRepository

class GetRelatedGrimoires:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    def execute(self) -> List[Grimoire]:
        return self.solicitud_repository.get_related_grimoires()