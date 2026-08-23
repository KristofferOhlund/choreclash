from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    """Subclasses of Base is will be established as a new ORM mapped class"""
    pass

class DB:
    def __init__(self):
        self.resource = "sqlite:///choreclash.db"
        self.engine = None

    def get_engine(self):
        """Create engine in module scope"""
        if not self.engine:
            self.engine = create_engine("sqlite:///choreclash.db")
        return self.engine


    def get_session(self):
        """return session factory"""
        if not self.engine:
            self.get_engine()
        return sessionmaker(self.engine)
