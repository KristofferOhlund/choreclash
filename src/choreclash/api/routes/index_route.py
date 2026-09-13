from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service


index_bp = Blueprint(
    "index",
    __name__,
)

db = DB()

@index_bp.get("/")
def index():
    return render_template("index.html")
    