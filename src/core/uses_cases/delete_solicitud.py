from src.core.Interfaces.solicitu_repository import SolicitudRepository

class DeleteSolicitud:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    def execute(self, solicitud_id: int):
        solicitud = self.solicitud_repository.get_by_id(solicitud_id)
        if not solicitud:
            raise ValueError(f"Solicitud con el id {solicitud_id} no encontrada.")

        self.solicitud_repository.delete(solicitud_id)
       
