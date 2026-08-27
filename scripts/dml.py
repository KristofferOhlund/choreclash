from choreclash.db.db import DB
from sqlalchemy.orm import Session
import choreclash.models as models
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
            chore_obj.append(models.Chore(title=chore['title'], description=chore['description'], icon=chore['icon']))
    try:
        session.add_all(chore_obj)
        session.commit()
    except Exception as e:
        print(f"Error occurred while adding chore : {e}")
        session.rollback()
