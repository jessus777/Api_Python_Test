from unittest.mock import MagicMock
from src.core.entities.grimoire import Grimoire
from src.core.uses_cases.get_all_grimoires import GetAllGrimoires

def test_get_all_grimoires():
    # Crear un mock del repositorio de grimorios
    grimoire_repository_mock = MagicMock()
    
    # Datos de ejemplo para los grimorios
    grimorio_1 = Grimoire(id='1', nombre='Grimorio 1', nivel=1)
    grimorio_2 = Grimoire(id='2', nombre='Grimorio 2', nivel=2)
    grimorio_3 = Grimoire(id='3', nombre='Grimorio 3', nivel=3)
    
    # Configurar el comportamiento esperado del repositorio mock
    grimoire_repository_mock.get_all.return_value = [grimorio_1, grimorio_2, grimorio_3]
    
    # Instanciar el caso de uso con el repositorio mock
    get_all_grimoires_use_case = GetAllGrimoires(grimoire_repository_mock)
    
    # Ejecutar el caso de uso
    result = get_all_grimoires_use_case.execute()
    
    print()
    print(result)

    # Verificar que se devuelvan los grimorios esperados
    assert len(result) == 3
    assert result[0].id == '1'
    assert result[1].id == '2'
    assert result[2].id == '3'
