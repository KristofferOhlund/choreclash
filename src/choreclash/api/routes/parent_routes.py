from flask import (
    Blueprint, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent


parent_bp = Blueprint(
    "parents",
    __name__,
)

db = DB()

@parent_bp.get("/home")
def home():
    user_id = session["user_id"]
    return render_template("home.html", user=user_id)
