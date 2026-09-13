"""
Chore service module for managing chores.
"""
from flask import session
from choreclash.models.chores import Chore
from choreclash.db.db import DB


def get_chore(chore_id: str):
    """
    Get a chore by its ID.

    Args:
        chore_id (str): The ID of the chore to be retrieved.
    """
    db = DB()
    with db.get_session() as db_session:
        chore = db_session.query(Chore).filter_by(id=chore_id).first()
        return chore

def get_chores():
    """
    Retrieve all chores for a given parent.

    Args:
        parent_id (str): The ID of the parent.

    Returns:
        list: A list of chore objects corresponding to the parent.
    """
    db = DB()
    with db.get_session() as db_session:
        chores = db_session.query(Chore).all()
        return chores


def update_chore(chore_id: str, updated_data: dict):
    """
    Update a chore

    Args:
        chore_id (str): The ID of the chore to be updated.
        updated_data (dict): A dictionary containing the updated chore data.
    """
    db = DB()
    with db.get_session() as db_session:
        chore = db_session.query(Chore).filter_by(id=chore_id).first()
        if chore:
            for key, value in updated_data.items():
                setattr(chore, key, value)
            db_session.commit()


def delete_chore(chore_id: str):
    """
    Delete a chore

    Args:
        chore_id (str): The ID of the chore to be deleted.
    """
    db = DB()
    with db.get_session() as db_session:
        chore = db_session.query(Chore).filter_by(id=chore_id).first()
        if chore:
            db_session.delete(chore)
            db_session.commit()