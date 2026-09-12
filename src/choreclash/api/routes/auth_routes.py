from flask import (
    Blueprint, render_template, request, flash)
from choreclash.api.services import auth_service
from choreclash.api.helpers.validators import validate_email, validate_passwords

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    print("user tries to login")
    if request.method == "POST":
        # hantera login
        pass

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        pass1 = request.form["password1"]
        pass2 = request.form["password2"]

        # verify email
        try:
            valid_email = validate_email(email)

            # verify passwords
            valid_passwords = validate_passwords(pass1, pass2)

            # Register user
            print("registrerar användare")

        except ValueError as e:
            flash(
                str(e),
                "error"
                )

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    return render_template("logout.html")

