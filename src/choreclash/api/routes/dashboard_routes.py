from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service, child_service


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
)

db = DB()

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    parent_id = session.get("parent_id")
    if not parent_id:
        return redirect("auth.login")

    children = child_service.get_all_children()
    print("HÄR ÄR BARNEN")
    for child in children:
        print(child.first_name)
    return render_template("dashboard.html", children=children)
    