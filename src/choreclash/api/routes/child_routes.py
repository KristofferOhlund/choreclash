from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.children import Child
from choreclash.api.services import child_service


child_bp = Blueprint(
    "child",
    __name__,
)

@child_bp.route("/child/create", methods=["GET", "POST"])
def create_child():
    parent_id = session.get("parent_id")
    if not parent_id:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        child_data = {
            "first_name": request.form.get("first_name"),
            "avatar_url": request.form.get("avatar_url"),
            "parent_id": parent_id
        }
        child_service.create_child(child_data)
        flash("Child created successfully.", "success")
        return redirect(url_for("parent.canvas"))

    return render_template("create_child.html")

@child_bp.route("/child/<int:child_id>", methods=["GET"])
def child_profile(child_id):
    child = child_service.get_child(child_id)
    if not child:
        flash("Child not found.", "error")
        return redirect(url_for("parent.canvas"))

    return render_template("child_profile.html", child=child)