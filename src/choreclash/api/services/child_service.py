"""
Child service module for managing children.
"""
from choreclash.models.children import Child
from choreclash.models.chore2child import Chore2Child
from choreclash.db.db import DB
from sqlalchemy import select
from sqlalchemy.orm import selectinload


def get_child(child_id: str):
    """
    Get a child and all of its relationship objects by its child ID.

    Args:
        child_id (str): The ID of the child to be retrieved.

    Returns:
        Child object with all of its sub objects (relationships)
    """

    
    db = DB()
    with db.get_session() as session:
        child = session.scalar(select(Child)
                .options(
                selectinload(Child.chore_assignments)
                .selectinload(Chore2Child.chore),
                selectinload(Child.chore_assignments)
                .selectinload(Chore2Child.occurrences))
        .where(Child.id == child_id))
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
    with db.get_session() as session:
        child = session.query(Child).filter_by(id=child_id).first()
        if child:
            for key, value in updated_data.items():
                setattr(child, key, value)
            session.commit()

def delete_child(child_id: str):
    """
    Delete a child

    Args:
        child_id (str): The ID of the child to be deleted.
    """
    db = DB()
    with db.get_session() as session:
        child = session.query(Child).filter_by(id=child_id).first()
        if child:
            session.delete(child)
            session.commit()

def create_child(child_data: dict):
    """
    Create a new child

    Args:
        child_data (dict): A dictionary containing the child data.
    """
    db = DB()

    with db.get_session() as session:
        new_child = Child(**child_data)
        session.add(new_child)
        session.commit()
