from typing import List
from src.core.entities.grimoire import Grimoire
from src.core.Interfaces.grimoire_repository import GrimoireRepository
from src.core.uses_cases.get_all_grimoires import GetAllGrimoires


class GrimoireService:
    def __init__(self, grimoire_repository: GrimoireRepository):
        #self.create_solicitud = CreateSolicitud(solicitud_repository)
        #self.update_solicitud = UpdateSolicitud(solicitud_repository)
        self.get_all_grimoires_use_case = GetAllGrimoires(grimoire_repository)


    #def create_solicitud(self, solicitud: Solicitud):
    #    self.create_solicitud.execute(solicitud)
#
    #def get_solicitud_by_id(self, solicitud_id: int) -> Solicitud:
    #    return self.solicitud_repository.get_by_id(solicitud_id)
#
    def get_all(self) -> List[Grimoire]:
        return   self.get_all_grimoires_use_case.execute()

    #def update_solicitud(self, solicitud: Solicitud):
    #    self.update_solicitud.execute(solicitud)
#
    #def delete_solicitud(self, solicitud_id: int):
    #    self.solicitud_repository.delete(solicitud_id)