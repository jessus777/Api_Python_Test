from src.core.Interfaces.solicitu_repository import SolicitudRepository
from src.core.Interfaces.grimoire_repository import GrimoireRepository
from src.core.entities.solicitud import Solicitud
from src.core.uses_cases.insert_solicitud import CreateSolicitud

class SolicitudService:
    def __init__(self, solicitud_repository: SolicitudRepository, grimoire_repository: GrimoireRepository):
        self.solicitud_repository = solicitud_repository
        self.grimoire_repository = grimoire_repository
        self.create_solicitud_use_case = CreateSolicitud(solicitud_repository, grimoire_repository)

    def create_solicitud(self, solicitud_data: dict) -> None:
        try:
            solicitud = Solicitud(**solicitud_data)
            self.create_solicitud_use_case.execute(solicitud)
        except ValueError as e:
            raise ValueError(f"Error al crear la solicitud: {str(e)}")    
        except Exception as e:
            raise Exception(f"Error inesperado al crear la solicitud: {str(e)}")
