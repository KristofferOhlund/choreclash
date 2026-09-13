from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service


parent_bp = Blueprint(
    "parent",
    __name__,
)

db = DB()

@parent_bp.get("/canvas")
def canvas():
    parent_id = session.get("parent_id")
    if not parent_id:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("auth.login"))

    # get children of the parent
    children = parent_service.get_children(parent_id)

    return render_template("canvas.html", children=children)
