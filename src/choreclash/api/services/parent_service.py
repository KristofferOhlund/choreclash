"""
Parent service module for user (parent)
"""

import email

from flask import session
from choreclash.models.parent import Parent
from choreclash.models.children import Child
from choreclash.db.db import DB

def get_parent(parent_id: str) -> Parent:
    """
    Retrieve a parent by their ID.

    Returns:
        Parent: The parent object corresponding to the logged-in user.
    """
    user_id = session.get("user_id")
    if not user_id:
        return None

    db = DB()
    with db.get_session() as db_session:
        parent = db_session.query(Parent).filter_by(id=parent_id).first()
        return parent

def get_children(parent_id: str) -> list[Child]:
    """
    Retrieve the children of a parent by their ID.

    Returns:
        list[Child]: A list of Child objects corresponding to the parent's children.
    """

    db = DB()
    with db.get_session() as db_session:
        parent = db_session.query(Parent).filter_by(id=parent_id).first()
        return parent.children