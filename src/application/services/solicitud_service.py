from typing import List
from src.core.Interfaces.solicitu_repository import SolicitudRepository
from src.core.Interfaces.grimoire_repository import GrimoireRepository
from src.core.entities.solicitud import Solicitud
from src.application.models.solicitud_create import SolicitudCreate
from src.application.models.solicitud_update import SolicitudUpdate
from src.core.uses_cases.insert_solicitud import CreateSolicitud
from src.core.uses_cases.update_solicitud import UpdateSolicitud
from src.core.uses_cases.patch_estatus_solicitud import PatchEstatusSolicitud
from src.core.uses_cases.get_all_solicitudes import GetAllSolicitudes

class SolicitudService:
    def __init__(self, solicitud_repository: SolicitudRepository, grimoire_repository: GrimoireRepository):
        self.solicitud_repository = solicitud_repository
        self.grimoire_repository = grimoire_repository
        self.create_solicitud_use_case = CreateSolicitud(solicitud_repository, grimoire_repository)
        self.get_solicitud_use_case = GetAllSolicitudes(solicitud_repository)
        self.update_solicitud_use_case = UpdateSolicitud(solicitud_repository)
        self.patch_state_solicitud_use_case = PatchEstatusSolicitud(solicitud_repository)

    def create_solicitud(self, solicitud_data: dict) -> None:
        try:
            solicitud = Solicitud(**solicitud_data)
            self.create_solicitud_use_case.execute(solicitud)
        except ValueError as e:
            raise ValueError(f"Error al crear la solicitud: {str(e)}")    
        except Exception as e:
            raise Exception(f"Error inesperado al crear la solicitud: {str(e)}")
        
    def update_solicitud(self,id_solicitud: int, solicitud_data: dict) -> SolicitudUpdate:
        try:
            solicitud = Solicitud(**solicitud_data)
            update_solicitud = self.update_solicitud_use_case.execute(id_solicitud, solicitud)
            solicitud_update = SolicitudUpdate(
                nombre= update_solicitud.nombre,
                apellido=update_solicitud.apellido,
                edad=update_solicitud.edad,
                identificacion=update_solicitud.identificacion,
                afinidad_magica=update_solicitud.afinidad_magica,
                estatus=update_solicitud.estatus
            )
            return solicitud_update
        except ValueError as e:
            raise ValueError(f"Error al crear la solicitud: {str(e)}")    
        except Exception as e:
            raise Exception(f"Error inesperado al crear la solicitud: {str(e)}")
        
    def patch_state_solicitud(self, solicitud_id: int, estatus: str) -> None:
        try:
            self.patch_state_solicitud_use_case.execute(solicitud_id, estatus)
        except ValueError as e:
            raise ValueError(f"Error al actualizar el estado solicitud: {str(e)}")    
        except Exception as e:
            raise Exception(f"Error al actualizar el estado solicitud: {str(e)}") 
    
        
    def get_list_request(self) -> List[Solicitud]:
        return self.get_solicitud_use_case.execute()
