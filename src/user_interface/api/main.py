from fastapi import FastAPI,  HTTPException
from src.application.models.solicitud_create import SolicitudCreate
from src.application.models.solicitud_update import SolicitudUpdate
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
        raise HTTPException(status_code=500, detail="Internal Server Error")   
    

@app.patch('/solicitudes/{solicitud_id}/estatus', description="Actualiza el estatus de una solicitud")
def patch_solicitud(solicitud_id: int, estatus: str):
    try:
        solicitud_service.patch_state_solicitud(solicitud_id, estatus)
        return {"message": "Solicitud actualizada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.put('/solicitudes/{solicitud_id}', description="Actualiza una solicitud")
def update_solicitud(
    solicitud_id: int,
    solicitud_data: SolicitudUpdate 
    ):
    try:
        solicitud_data_dict = solicitud_data.model_dump()
        updated_solicitud = solicitud_service.update_solicitud(solicitud_id, solicitud_data_dict)
        return updated_solicitud
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.delete('/solicitudes/{solicitud_id}', description="Elimina una solicitud")
def delete_solicitud(solicitud_id: int):
    try:
        solicitud_service.delete_solicitud(solicitud_id)
        return {"message": "Solicitud eliminada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get('/solicitudes', description="Obtiene las solicitudes")
def get_all_solicitudes():
    solicitudes = solicitud_service.get_list_request()
    return solicitudes

@app.get('/grimoires', description="Obtiene los grimoires")
def get_all_grimoires():
    grimoires = grimoires_service.get_all()
    return grimoires

@app.get('/asignaciones', description="Obtiene todos los grimorios asignados con solicitudes")
def get_all_related_grimoires():
    try:
        grimoires = solicitud_service.get_related_grimoires()
        return grimoires
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")