from src.infrastructure.database.config.connection import DBConnectionHandler
from .grimoire_repository_impl import GrimoireRepositoryImpl

def test_insert_grimoires():

    students_repository = GrimoireRepositoryImpl()
    grimoires = students_repository.get_all()

    print()
    print(grimoires)

    assert True

