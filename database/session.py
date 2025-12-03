from sqlmodel import Session, SQLModel, create_engine
from contextlib import contextmanager
from typing import Generator, Optional, Union
from sqlalchemy import Engine

class MySession:
    
    database_name: str = "database.db"
    driver: str = "sqlite"
    engine: Optional[Engine] = None
    
    @classmethod
    def _init_engine(cls):
        if cls.engine is None:
            cls.engine = create_engine(f"{cls.driver}:///{cls.database_name}", echo=True)
        return cls.engine

    @classmethod
    def create_db(cls):
        cls._init_engine()
        SQLModel.metadata.create_all(cls.engine)
    
    @classmethod
    def get_session(cls) -> Generator[Session, None, None]:
        cls._init_engine()
        session = Session(cls.engine)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
            
    @classmethod
    @contextmanager
    def session_scope(cls) -> Generator[Session, None, None]:
        with cls.get_session() as session:
            yield session
            
    @classmethod
    def commit(cls, *args, **kwargs):
        with cls.get_session as session:
            for arg in args:
                session.add(arg)
                
    @classmethod
    def execute(cls, query):
        with cls.get_session as session:
            return session.exec(query).first()
        
    @classmethod
    def execute_all(cls, query):
        with cls.get_session as session:
            return tuple(session.exec(query).all())
    
MySession.create_db()