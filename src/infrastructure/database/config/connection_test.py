from .connection import DBConnectionHandler

def test_get_engine_conection():
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    print()
    print(engine)
    assert engine is not None