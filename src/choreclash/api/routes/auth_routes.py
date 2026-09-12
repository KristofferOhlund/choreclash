from flask import (
    Blueprint, render_template, request, flash, url_for)
from choreclash.api.services import auth_service
from choreclash.db.db import DB


auth_bp = Blueprint(
    "auth",
    __name__
)

db = DB()

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            with db.get_session() as session:
                user = auth_service.authenticate_user(session, request.form)
        except ValueError as e:
            flash(
                str(e),
                "error"
                )
        return url_for("user.home")

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            with db.get_session() as session:
                auth_service.create_user(session, request.form)
        except ValueError as e:
            flash(
                str(e),
                "error"
                )
        return url_for("auth.login")

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    return render_template("logout.html")

