"""
Auth service module for user (parent) registration and authentication.
"""

import email

from flask import session
from choreclash.models.parent import Parent
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