"""
Child service module for managing children.
"""
from flask import session
from choreclash.models.children import Child
from choreclash.db.db import DB


def get_child(child_id: str):
    """
    Get a child by its ID.

    Args:
        child_id (str): The ID of the child to be retrieved.
    """
    db = DB()
    with db.get_session() as db_session:
        child = db_session.query(Child).filter_by(id=child_id).first()
        return child

def update_child(child_id: str, updated_data: dict):
    """
    Update a child

    Args:
        child_id (str): The ID of the child to be updated.
        updated_data (dict): A dictionary containing the updated child data.
    """
    raise NotImplementedError("This function is not yet implemented.")
    db = DB()
    with db.get_session() as db_session:
        child = db_session.query(Child).filter_by(id=child_id).first()
        if child:
            for key, value in updated_data.items():
                setattr(child, key, value)
            db_session.commit()

def delete_child(child_id: str):
    """
    Delete a child

    Args:
        child_id (str): The ID of the child to be deleted.
    """
    db = DB()
    with db.get_session() as db_session:
        child = db_session.query(Child).filter_by(id=child_id).first()
        if child:
            db_session.delete(child)
            db_session.commit()

def create_child(child_data: dict):
    """
    Create a new child

    Args:
        child_data (dict): A dictionary containing the child data.
    """
    db = DB()

    with db.get_session() as db_session:
        new_child = Child(**child_data)
        db_session.add(new_child)
        db_session.commit()


def get_chore_assignments(child_id: int):
    """
    Get chore assignments for a child

    Args:
        child_id (int): The ID of the child whose chore assignments are to be retrieved.
    """
    db = DB()
    with db.get_session() as db_session:
        child = db_session.query(Child).filter_by(id=child_id).first()
        if child:
            return child.chore_assignments
        return []