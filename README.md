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

- Python 3.8 o superior.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- Sql Server ver. 15 o superior.
### Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/jessus777/Api_Python_Test.git
   cd tu_repositorio

2.  Crear y activar un entorno virual en Windows
    ```bash
    python -m venv env
    .\venv\Scripts\activate


3. Instalar dependencias
      pip install -r requirements.txt


4. Ejecutar el script en un entorno de sql server management (en el servidor de preferencia el servidor local, con autentificacion de windows)
    src/db/database.sql


## Ejecucion de la aplicaion

2. Verifica la cadena de conexión:
   ```bash
   # src/infraestructure/database/config/connection.py
    self.__connection_string = 'mssql+pyodbc://{Server_Name}/{Data_Base}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

    'trusted_connection=yes: Indica que se utilizará la autenticación integrada de Windows (trusted_connection). Esto significa que se usarán las credenciales de Windows actuales para autenticarse en SQL Server. No se especifica un usuario ni contraseña explícitamente en la cadena de conexión, confiando en la autenticación de Windows.'

2. Para ejecutar la aplicación con FastAPI debe ejecutar el servidor de la siguiente manera:

  ```bash
    uvicorn src.user_interface.api.main:app


## Endpoints Disponibles

1. GET /solicitudes: Obtiene todas las solicitudes.
2. POST /solicitudes: Crea una nueva solicitud.
3. PATCH /solicitudes/{solicitud_id}/estatus: Actualiza el estado de una solicitud.
4. DELETE /solicitudes/{solicitud_id}: Elimina una solicitud.
5. GET /grimoires: Obtiene todos los grimorios.
6. GET /asignaciones: Obtiene todos los grimorios asignados a las solicitudes.

