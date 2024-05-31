from abc import ABC, abstractmethod
from typing import List
from src.core.entities.grimoire import Grimoire

class GrimoireRepository(ABC):
    @abstractmethod
    def add(self, grimoire: Grimoire):
        pass

    @abstractmethod
    def get_by_id(self, grimoire_id: str) -> Grimoire:
        pass

    @abstractmethod
    def get_all(self) -> List[Grimoire]:
        pass

    @abstractmethod
    def update(self, grimoire: Grimoire):
        pass

    @abstractmethod
    def delete(self, grimoire_id: str):
        pass
