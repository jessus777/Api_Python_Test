# src/infrastructure/database/init_db.py
import sys
import os

# Asegura que la ruta raíz del proyecto esté en sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.infrastructure.database.config.connection import DBConnectionHandler
from src.infrastructure.database.config.base import Base
from src.core.entities.grimoire import Grimoire
from src.core.entities.solicitud import Solicitud

def init_db():
    db_handler = DBConnectionHandler()
    engine = db_handler.get_engine()
    Base.metadata.create_all(engine)

    # Crear algunos registros de ejemplo
    grimoires = [
        Grimoire(nombre='Códice de lo Arcano', nivel=1),
        Grimoire(nombre='Tomo de la Sabiduría Antigua', nivel=2),
        Grimoire(nombre='Libro de Hechizos Perdidos', nivel=3),
         Grimoire(nombre='Grimorio de Encantamientos', nivel=4),
        Grimoire(nombre='Necronomicón', nivel=5),
        Grimoire(nombre='Libro de Sombras', nivel=6)
    ]

    with db_handler as db:
         # Eliminar todos los registros existentes en las tablas
        db.session.query(Solicitud).delete()
        db.session.query(Grimoire).delete()
        db.session.commit()

        existing_grimoires = db.session.query(Grimoire).all()
        if not existing_grimoires:
            db.session.add_all(grimoires)
            db.session.commit()
            print('Grimoires added successfully')
        else:
            print('Grimoires already exist')

if __name__ == "__main__":
    init_db()
