"""
Chore2Child service module for managing Chore2Child objects.
"""
from flask import session
from choreclash.models import Chore2Child, ChoreOccurence

from choreclash.db.db import DB

def delete_chore2child(child_id: str):
    """
    Delete a chore2child association by its ID.
    """
    raise NotImplementedError("This function is not yet implemented.")

def create_chore2child(child_ids: list, chore_ids: list):
    """
    Create Chore2Child object based on list of child_ids, chore_ids

    Args:
        child_ids: list of Child ids: ["1", "2", "3"]
        choreids: list of Chore ids: ["1", "2", "3"]

    Returns:
        list of Chore2Child objects
    """

    db = DB()
    c2c_objects = []
    try:
        with db.get_session() as session:
            for c_id in child_ids:
                for ch_id in chore_ids:
                    chore2child = Chore2Child(child_id=c_id, chore_id=ch_id)
                    c2c_objects.append(chore2child)
                    session.add(chore2child)
            session.commit()
    except Exception as e:
        print(f"Error creating chore2child: {e}")
        session.rollback()

    return c2c_objects