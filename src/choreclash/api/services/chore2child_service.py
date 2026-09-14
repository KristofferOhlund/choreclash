"""
Child service module for managing children.
"""
from flask import session
from choreclash.models.children import Child
from choreclash.db.db import DB

def delete_chore2child(child_id: str):
    """
    Delete a chore2child association by its ID.
    """
    raise NotImplementedError("This function is not yet implemented.")

def create_chore2child(child_data: dict):
    """
    Create a new chore2child association.

    Args:
        child_data (dict): A dictionary containing the child data.
    """
    raise NotImplementedError("This function is not yet implemented.")
