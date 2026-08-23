from db.db import Base, DB
from models.children import Child
from models.chores import Chore
from models.parent import Parent


# Create all tables from ORM
db = DB()
engine = db.get_engine()
Base.metadata.create_all(engine)

print("tabeller skapade")