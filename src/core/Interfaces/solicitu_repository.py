from abc import ABC, abstractmethod
from typing import List
from src.core.entities.solicitud import Solicitud
from src.core.entities.grimoire import Grimoire

class SolicitudRepository(ABC):
    @abstractmethod
    def add(self, solicitud: Solicitud):
        pass

    @abstractmethod
    def get_by_id(self, solicitud_id: int) -> Solicitud:
        pass

    @abstractmethod
    def get_all(self) -> List[Solicitud]:
        pass

    @abstractmethod
    def update(self, solicitud: Solicitud):
        pass

    @abstractmethod
    def delete(self, solicitud_id: int):
        pass
    @abstractmethod
    def get_related_grimoires(self) -> List[Grimoire]:
        pass
