from fastapi import FastAPI
from src.application.services.grimoire_service import GrimoireService
from src.infrastructure.repositories.grimoire_repository_impl import GrimoireRepositoryImpl

app = FastAPI()

grimoire_repository = GrimoireRepositoryImpl()

grimoires_service = GrimoireService(grimoire_repository)

@app.get('/grimoires', description="Get all grimoires")
def get_all_grimoires():
    grimoires = grimoires_service.get_all()
    return grimoires