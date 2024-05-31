from typing import List
from src.core.entities.grimoire import Grimoire
from src.core.Interfaces.grimoire_repository import GrimoireRepository

class GetAllGrimoires:
    def __init__(self, grimoire_repository: GrimoireRepository):
        self.grimoire_repository = grimoire_repository

    def execute(self) -> List[Grimoire]:
        return self.grimoire_repository.get_all()
