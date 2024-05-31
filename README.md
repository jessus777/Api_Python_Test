# Api_Python_Test
web api en python

# Proyecto de Gestión de Solicitudes y Grimorios

Este proyecto es una aplicación basada en Python que permite gestionar solicitudes y grimorios. Está estructurado utilizando principios de arquitectura limpia y se implementa con FastAPI y SQLAlchemy.

## Estructura del Proyecto


## Descripción de Carpetas y Archivos

- **core/**: Contiene las entidades y interfaces del núcleo de la aplicación.
  - **entities/**:
    - `solicitud.py`: Define la entidad Solicitud.
    - `grimoire.py`: Define la entidad Grimoire.
  - **interfaces/**:
    - `solicitud_repository.py`: Define la interfaz del repositorio de solicitudes.
  - **services/**:
    - `solicitud_service.py`: Define los servicios relacionados con las solicitudes.
- **infrastructure/**: Contiene las implementaciones concretas y el manejo de la base de datos.
  - **repositories/**:
    - `solicitud_repository_impl.py`: Implementa la interfaz del repositorio de solicitudes.
  - **db/**:
    - `db_handler.py`: Maneja la conexión y configuración de la base de datos.
- **api/**: Contiene la configuración de la API utilizando FastAPI.
  - `main.py`: Define los endpoints de la API.
- **db/**:
  - `database.sql`: Contiene el script SQL para la creación de la base de datos.
- **requirements.txt**: Lista las dependencias del proyecto.
- **README.md**: Proporciona información sobre el proyecto.

## Configuración del Proyecto

### Requisitos

- Python 3.8 o superior
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/jessus777/Api_Python_Test.git
   cd tu_repositorio

2.  Crear y activar un entorno virual
    python -m venv env
    
    source env/bin/activate  # En Windows: env\Scripts\activate

3. Instalar dependencias
    pip install -r requirements.txt

4. Ejecutar el script en un entorno de sql server
    src/db/database.sql

## Ejecucion de la aplicaion

1. Para ejecutar la aplicación con FastAPI:

    uvicorn src.user_interface.api.main:app


## Endpoints Disponibles

1. GET /solicitudes: Obtiene todas las solicitudes.
2. GET /solicitudes/{solicitud_id}: Obtiene una solicitud por su ID.
3. POST /solicitudes: Crea una nueva solicitud.
4. PATCH /solicitudes/{solicitud_id}: Actualiza el estado de una solicitud.
5. DELETE /solicitudes/{solicitud_id}: Elimina una solicitud.
6. GET /grimoires: Obtiene todos los grimorios relacionados con las solicitudes.

