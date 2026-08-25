from choreclash.db.db import Base, DB
# imports are needed to register the models with the Base metadata
from choreclash.models.children import Child
from choreclash.models.parent import Parent
from choreclash.models.chore_template import ChoreTemplate
from choreclash.models.chore_assignment import ChoreAssignment


# Create all tables from ORM
db = DB()
engine = db.get_engine()
Base.metadata.create_all(engine)

print("tabeller skapade")