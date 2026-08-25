from sqlalchemy.orm import Session
from choreclash.db.db import Base, DB
from choreclash.models.chore_template import ChoreTemplate

db = DB().get_engine()
with Session(db) as session:
    # Get all chores
    chores = session.query(ChoreTemplate).all()
    for chore in chores:
        print(f"Chore ID: {chore.get_id()}, Title: {chore.get_title()}, Description: {chore.get_description()}, Icon: {chore.get_icon()}, Is Complete: {chore.get_is_complete()}, Deadline: {chore.get_deadline()}")