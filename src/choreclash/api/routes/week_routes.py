from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service


week_bp = Blueprint(
    "week",
    __name__,
)

db = DB()

@week_bp.route("/week", methods=["GET"])
def week():
    parent_id = session.get("parent_id")
    if not parent_id:
        return redirect("auth.login")
    return render_template("week.html")
    