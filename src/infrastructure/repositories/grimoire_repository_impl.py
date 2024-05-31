import logging
from typing import List
from sqlalchemy.orm import Session
from src.core.entities.grimoire import Grimoire
from src.core.Interfaces.grimoire_repository import GrimoireRepository
from src.infrastructure.database.config.connection import DBConnectionHandler

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GrimoireRepositoryImpl(GrimoireRepository):
    def __init__(self):
        self.db_handler = DBConnectionHandler()

    def add(self, grimoire: Grimoire):
        try:
            with self.db_handler as db:
                db.session.add(grimoire)
                db.session.commit()
                logger.info(f'Grimoire added successfully: {grimoire}')
        except Exception as e:
            logger.error(f'Error adding grimoire: {e}')
            raise e

    def get_by_id(self, grimoire_id: str) -> Grimoire:
        try:
            with self.db_handler as db:
                grimoire = db.session.query(Grimoire).filter_by(id=grimoire_id).first()
                logger.info(f'Fetched grimoire by id {grimoire_id}: {grimoire}')
                return grimoire
        except Exception as e:
            logger.error(f'Error fetching grimoire by id {grimoire_id}: {e}')
            raise e

    def get_all(self) -> List[Grimoire]:
        try:
            with self.db_handler as db:
                grimoires = db.session.query(Grimoire).all()
                logger.info('Fetched all grimoires')
                return grimoires
        except Exception as e:
            logger.error(f'Error fetching all grimoires: {e}')
            raise e

    def update(self, grimoire: Grimoire):
        try:
            with self.db_handler as db:
                db.session.merge(grimoire)
                db.session.commit()
                logger.info(f'Grimoire updated successfully: {grimoire}')
        except Exception as e:
            logger.error(f'Error updating grimoire: {e}')
            raise e

    def delete(self, grimoire_id: str):
        try:
            with self.db_handler as db:
                grimoire = db.session.query(Grimoire).filter_by(id=grimoire_id).first()
                if grimoire:
                    db.session.delete(grimoire)
                    db.session.commit()
                    logger.info(f'Grimoire deleted successfully: {grimoire_id}')
        except Exception as e:
            logger.error(f'Error deleting grimoire by id {grimoire_id}: {e}')
            raise e
