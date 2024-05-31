import random
from src.core.entities.solicitud import Solicitud
from src.core.entities.grimoire import Grimoire
from src.core.Interfaces.solicitu_repository import SolicitudRepository
from src.core.Interfaces.grimoire_repository import GrimoireRepository


class CreateSolicitud:
    def __init__(self, solicitud_repository: SolicitudRepository, grimoire_repository: GrimoireRepository):
        self.solicitud_repository = solicitud_repository
        self.grimoire_repository = grimoire_repository

    def execute(self, solicitud: Solicitud):
        self.__validate_first_name(solicitud.nombre)
        self.__validate_last_name(solicitud.apellido)
        self.__validate_age(solicitud.edad)
        self.__validate_affinity(solicitud.afinidad_magica) 
        
    
        grimorios = self.grimoire_repository.get_all()

        if not grimorios:
            raise ValueError("No hay grimorios disponibles.")

        grimorio_seleccionado = random.choice(grimorios)
        
        solicitud.grimorio_id = grimorio_seleccionado.id
        self.solicitud_repository.add(solicitud)


    @classmethod
    def __validate_first_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise ValueError('Nombre invalido')
        
        if len(first_name) > 20:
            raise ValueError('Nombre muy extenso')

    @classmethod
    def __validate_last_name(cls, last_name: str) -> None:
        if not last_name.isalpha():
            raise ValueError('Nombre invalido')
        
        if len(last_name) > 20:
            raise ValueError('Nombre muy extenso')
        
    @classmethod
    def __validate_age(cls, age: int) -> None:
        if not isinstance(age, int):
            raise ValueError('Edad no es un número entero')

        if not (10 <= age <= 99):
            raise ValueError('Edad no tiene dos dígitos')
    
    @classmethod
    def __validate_affinity(cls, affinity: str) -> None:
        allowed_affinities = {"Oscuridad", "Luz", "Agua"}
        if affinity not in allowed_affinities:
            raise ValueError(f'Afinidad Magica inválida. Debe ser una de {", ".join(allowed_affinities)}')
