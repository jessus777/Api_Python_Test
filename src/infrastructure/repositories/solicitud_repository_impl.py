import logging
from typing import List
from sqlalchemy.orm import Session
from src.core.entities.solicitud import Solicitud
from src.core.Interfaces.solicitu_repository import SolicitudRepository
from src.infrastructure.database.config.connection import DBConnectionHandler

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolicitudRepositoryImpl(SolicitudRepository):
    def __init__(self):
        self.db_handler = DBConnectionHandler()

    def add(self, solicitud: Solicitud):
        try:
            with self.db_handler as db:
                db.session.add(solicitud)
                db.session.commit()
                logger.info(f'Solicitud added successfully: {solicitud}')
        except Exception as e:
            logger.error(f'Error adding solicitud: {e}')
            raise e

    def get_by_id(self, solicitud_id: int) -> Solicitud:
        try:
            with self.db_handler as db:
                solicitud = db.session.query(Solicitud).filter_by(id=solicitud_id).first()
                logger.info(f'Fetched solicitud by id {solicitud_id}: {solicitud}')
                return solicitud
        except Exception as e:
            logger.error(f'Error fetching solicitud by id {solicitud_id}: {e}')
            raise e

    def get_all(self) -> List[Solicitud]:
        try:
            with self.db_handler as db:
                solicitudes = db.session.query(Solicitud).all()
                logger.info('Fetched all solicitudes')
                return solicitudes
        except Exception as e:
            logger.error('Error fetching all solicitudes: {e}')
            raise e

    def update(self, solicitud: Solicitud):
        try:
            with self.db_handler as db:
                db.session.merge(solicitud)
                db.session.commit()
                logger.info(f'Solicitud updated successfully: {solicitud}')
        except Exception as e:
            logger.error(f'Error updating solicitud: {e}')
            raise e

    def delete(self, solicitud_id: int):
        try:
            with self.db_handler as db:
                solicitud = db.session.query(Solicitud).filter_by(id=solicitud_id).first()
                if solicitud:
                    db.session.delete(solicitud)
                    db.session.commit()
                    logger.info(f'Solicitud deleted successfully: {solicitud_id}')
        except Exception as e:
            logger.error(f'Error deleting solicitud by id {solicitud_id}: {e}')
            raise e
