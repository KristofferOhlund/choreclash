from choreclash.db.db import Base, DB
# imports are needed to register the models with the Base metadata
import choreclash.models as models
from sqlalchemy import inspect


# Create all tables from ORM
db = DB()
engine = db.get_engine()
Base.metadata.create_all(engine)

# Make sure they are created
print("tabeller i databasen:")
print(Base.metadata.tables.keys())