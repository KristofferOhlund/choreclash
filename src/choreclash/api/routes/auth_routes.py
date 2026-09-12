from flask import (
    Blueprint, render_template, request, flash, url_for, redirect, session)
from choreclash.api.services import auth_service
from choreclash.api.routes import parent_routes
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
            user = auth_service.authenticate_user(request.form)
            session["user_id"] = user.id
        except ValueError as e:
            flash(
                str(e),
                "error"
                )
        return redirect(url_for("parents.home"))

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            auth_service.create_user(request.form)
        except ValueError as e:
            flash(
                str(e),
                "error"
                )
        return url_for("auth.login")

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")

