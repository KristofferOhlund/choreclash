from choreclash.db.db import Base, DB
from sqlalchemy.orm import Session
from choreclash.models.chore_template import ChoreTemplate
from choreclash.models.chore_assignment import ChoreAssignment
from choreclash.models.parent import Parent
from choreclash.models.children import Child
import json

# Get engine object
engine = DB().get_engine()

# DML (Data Manipulation Language) = datan (INSERT, UPDATE, DELETE, SELECT)

## INSERT into chore_template_table
with Session(engine) as session:
    chore_obj = []
    with open('scripts/data/chores.json') as f:
        chores = json.load(f)
        for chore in chores:
            chore_obj.append(ChoreTemplate(title=chore['title'], description=chore['description'], icon=chore['icon']))
    try:
        session.add_all(chore_obj)
        session.commit()
    except Exception as e:
        print(f"Error occurred while adding chore templates: {e}")
        session.rollback()
