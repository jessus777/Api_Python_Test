from src.core.Interfaces.solicitu_repository import SolicitudRepository

class PatchEstatusSolicitud:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    def execute(self, solicitud_id: int, estatus: str):
        solicitud = self.solicitud_repository.get_by_id(solicitud_id)
        if not solicitud:
            raise ValueError(f"Solicitud con el id {solicitud_id} no encontrada.")

        self.__validate_status(estatus)
        
        solicitud.estatus = estatus
        self.solicitud_repository.update(solicitud)
        return solicitud

    @classmethod
    def __validate_status(cls, status: str) -> None:
        if status is None or status.strip() == "":
            raise ValueError("El estatus no puede ser nulo o vacío.")
        
        valid_statuses = {"Registrado", "Cancelado", "Confirmado"}
        if status not in valid_statuses:
            raise ValueError(f"Estatus inválido. Debe ser uno de {', '.join(valid_statuses)}")