from typing import Optional
from src.core.entities.solicitud import Solicitud
from src.core.Interfaces.solicitu_repository import SolicitudRepository

class UpdateSolicitud:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    def execute(self, solicitud_id: int, solicitud: Solicitud):
        get_solicitud = self.solicitud_repository.get_by_id(solicitud_id)
        if not get_solicitud:
            raise ValueError(f"Solicitud con el id {solicitud_id} no encontrada.")
        
        self.__validate_first_name(solicitud.nombre)
        self.__validate_last_name(solicitud.apellido)
        self.__validate_identificator(solicitud.identificacion)
        self.__validate_age(solicitud.edad)
        self.__validate_affinity(solicitud.afinidad_magica) 
        self.__validate_status(solicitud.estatus)
        id_grioire = get_solicitud.grimoire_id
        get_solicitud.nombre = solicitud.nombre
        get_solicitud.apellido = solicitud.apellido
        get_solicitud.edad = solicitud.edad
        get_solicitud.identificacion = solicitud.identificacion
        get_solicitud.estatus = solicitud.estatus
        get_solicitud.afinidad_magica = solicitud.afinidad_magica
        #get_solicitud.grimoire_id = id_grioire
    
        print("que hay")
        print(f"id dell id grimoire: {id_grioire}")
        print(f"id dell grimoire: {get_solicitud.grimoire_id}")
        self.solicitud_repository.update(get_solicitud)
        return get_solicitud

    @classmethod
    def __validate_first_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise ValueError('Nombre invalido')
        
        if len(first_name) > 20:
            raise ValueError('Nombre muy extenso. No debe exceder el limite de 20 caracteres')

    @classmethod
    def __validate_last_name(cls, last_name: str) -> None:
        if not last_name.isalpha():
            raise ValueError('Apellido invalido')
        
        if len(last_name) > 20:
            raise ValueError('Apellido muy extenso. No debe exceder el limite de 20 caracteres')
        
    @classmethod
    def __validate_age(cls, age: int) -> None:
        if not isinstance(age, int):
            raise ValueError('Edad no es un número entero')

        if not (10 <= age <= 99):
            raise ValueError('Edad no tiene dos dígitos. Tiene que ser mayor de edad')
    
    @classmethod
    def __validate_affinity(cls, affinity: str) -> None:
        allowed_affinities = {"Oscuridad", "Luz", "Agua"}
        if affinity not in allowed_affinities:
            raise ValueError(f'Afinidad Magica inválida. Debe ser una de {", ".join(allowed_affinities)}')
        
    @classmethod
    def __validate_identificator(cls, identificator: str) -> None:
        if not identificator.isalnum():
            raise ValueError('Identificador invalido')
        
        if len(identificator) > 10:
        
            raise ValueError('Identificador muy extenso. No debe exceder el limite de 10 caracteres alfanumericos')
    @classmethod
    def __validate_status(cls, affinity: str) -> None:
        states = {"Registrado", "Cancelado", "Confirmado"}
        if affinity not in states:
            raise ValueError(f'Afinidad Magica inválida. Debe ser una de {", ".join(states)}')
        