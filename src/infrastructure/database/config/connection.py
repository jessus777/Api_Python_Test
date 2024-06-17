
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///test_database.db'
        self.__engine = create_engine(self.__connection_string, echo=True)
        self.__Session = sessionmaker(bind=self.__engine)
        self.session = None

    def __enter__(self):
        self.session = self.__Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.__engine
