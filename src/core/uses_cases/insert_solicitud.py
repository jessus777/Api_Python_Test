from typing import List
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
        self.__validate_identificator(solicitud.identificacion)
        self.__validate_age(solicitud.edad)
        self.__validate_affinity(solicitud.afinidad_magica) 
        
    
        grimorios = self.get_all_grimoros()

        if not grimorios:
            raise ValueError("No hay grimorios disponibles.")
        

        indice_aleatorio = random.randint(0, len(grimorios) - 1)
        grimorio_seleccionado_id = grimorios[indice_aleatorio].id

        solicitud.grimoire_id = grimorio_seleccionado_id
        self.solicitud_repository.add(solicitud)


    def get_all_grimoros(self)-> List[Grimoire]:
        return self.grimoire_repository.get_all()



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
        
    @classmethod
    def __validate_identificator(cls, identificator: str) -> None:
        if not identificator.isalnum():
            raise ValueError('identificador invalido')
        
        if len(identificator) > 10:
            raise ValueError('identificador muy extenso')
