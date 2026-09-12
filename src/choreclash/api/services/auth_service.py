"""
Auth service module for user (parent) registration and authentication.
"""

import email

from flask import session

from choreclash.api.helpers.validators import validate_email, validate_passwords, validate_string
from choreclash.models.parent import Parent
from choreclash.db.db import DB

def create_user(form_data):
    """
    Create a new user in the database.

    Args:
        session: The database session.
        form: The form data containing user information.

    Returns:
        None
    """
    fname = form_data["first_name"]
    lname = form_data["last_name"]
    email = form_data["email"]
    pass1 = form_data["password"]
    pass2 = form_data["confirm_password"]

    # verify all input
    validate_string(fname, "First name")
    validate_string(lname, "Last name")
    validate_email(email)
    validate_passwords(pass1, pass2)

    # Register user
    parent = Parent(first_name=fname, last_name=lname, email=email, password_hash=pass1)
    try:
        db = DB()
        with db.get_session() as session:
            session.add(parent)
            session.commit()
        print(f"User {fname} {lname} registered successfully.")
    except Exception as e:
        print(f"Error occurred while registering user: {e}")
        raise e
    
    print("registrerar användare")

def authenticate_user(form_data):
    """
    Authenticate a user based on the provided form data.

    Args:
        session: The database session.
        form_data: The form data containing user credentials.

    Returns:
        None
    """
    email = form_data["email"]
    password = form_data["password"]

    # verify all input
    validate_email(email)
    validate_string(password, "Password")

    # Authenticate user
    db = DB()
    with db.get_session() as session:
        parent = session.query(Parent).filter_by(email=email).first()
    if parent is None or parent.password_hash != password:
        raise ValueError("Invalid email or password.")

    print(f"User {parent.first_name} {parent.last_name} authenticated successfully.")

    return parent