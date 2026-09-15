"""
Child service module for managing children.
"""
from flask import session
from choreclash.models.chore2child import Chore2Child
from choreclash.models.children import Child
from choreclash.models.chores import Chore
from choreclash.db.db import DB

def delete_chore2child(child_id: str):
    """
    Delete a chore2child association by its ID.
    """
    raise NotImplementedError("This function is not yet implemented.")

def create_chore2child(child_data: list):
    """
    Create a new chore2child association.

    Args:
        child_data (list): A list containing the child data.
    """
    child_id = child_data.getlist("child_id")
    chore_id = child_data.getlist("chore_id")

    db = DB()
    try:
        with db.get_session() as session:
            for c_id in child_id:
                for ch_id in chore_id:
                    chore2child = Chore2Child(child_id=c_id, chore_id=ch_id)
                    session.add(chore2child)
            session.commit()
    except Exception as e:
        print(f"Error creating chore2child: {e}")
        session.rollback()