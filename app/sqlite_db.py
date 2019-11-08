from contextlib import contextmanager

from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SqliteDB(metaclass=Singleton):
    """
    # Provide access to sqlite database
    # Using SQLAlchemy library
    # Exposing engine to manage the pool of connection to the database
    # Exposing orm_base for Object Relational Mapping
    # Exposing sesh_factory for managing database transaction 
    # 
    """
    # self.uri: File path to sqlite database
    # self.engine: SQLAlchemy database engine object
    # self.orm_base: SQLAlchemy Object Relation Mapper object
    # self.sesh_factory: SQLAlchemy Session factory object

    def __init__(self):
        self.uri = None
        self.engine = None
        self.orm_base = None
        self.sesh_factory = None

    def __del__(self):
        self.disconnect()

    # Establish connection to database & initialize other variables
    def connect(self, uri, echo=False):
        self.disconnect()

        if uri != None:
            try:
                self.uri = uri
                self.engine = create_engine(uri, echo=echo)
            except Exception as e:
                print("%s: could not connect to %s" % (e, uri))

            self.orm_base = declarative_base(bind=self.engine)
            self.sesh_factory = sessionmaker(bind=self.engine)
            print("database connected")

    # Disconnect from the currect database & free up related variables
    def disconnect(self):
        if self.engine is not None:
            self.engine.dispose()

        self.sesh_factory = None
        self.orm_base = None
        self.engine = None
        self.uri = None

    # Acquiring a connection from the Engine's connection pool
    @contextmanager
    def get_conn(self):
        conn = self.engine.connect()
        try:
            yield conn
        except:
            raise
        finally:
            conn.close()

    # A context manager for session objects
    @contextmanager
    def get_sesh(self):
        session = self.sesh_factory()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def is_connected(self):
        if self.engine is not None:
            return True
        else:
            return False
