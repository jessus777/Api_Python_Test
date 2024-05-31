from fastapi import FastAPI,  HTTPException
from src.application.models.solicitud_create import SolicitudCreate
from src.application.services.grimoire_service import GrimoireService
from src.application.services.solicitud_service import SolicitudService
from src.infrastructure.repositories.grimoire_repository_impl import GrimoireRepositoryImpl
from src.infrastructure.repositories.solicitud_repository_impl import SolicitudRepositoryImpl

app = FastAPI()

grimoire_repository = GrimoireRepositoryImpl()
solicitud_repository = SolicitudRepositoryImpl()

grimoires_service = GrimoireService(grimoire_repository)
solicitud_service = SolicitudService(solicitud_repository, grimoire_repository)


@app.post('/solicitudes', description="Crea una solicitud")
def add_solicitud(solicitud_data: SolicitudCreate):
    try:
        solicitud_data_dict = solicitud_data.model_dump()
        solicitud_service.create_solicitud(solicitud_data_dict)
        return {"message": "Solicitud creada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor: " + str(e))


@app.get('/grimoires', description="Get all grimoires")
def get_all_grimoires():
    grimoires = grimoires_service.get_all()
    return grimoires