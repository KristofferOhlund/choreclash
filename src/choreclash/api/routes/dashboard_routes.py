from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service, child_service, occurence_service
from choreclash.api.helpers.helpers import get_dates_in_current_week, get_days_from_dates


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

    # Current Week dates
    week_dates = get_dates_in_current_week()

    # Day headers
    header_days = get_days_from_dates(week_dates)
   
    # Chore Occurences
    chore_occurences = occurence_service.get_chore_occurences_by_week(parent_id=parent_id)

    # All chores for the day is completed
    days_where_chores_are_complete = occurence_service.check_daily_chores_complete(chore_occurences)
    print(days_where_chores_are_complete)

    return render_template("dashboard.html", 
                           chores=chore_occurences, week_dates=week_dates, header_days=header_days,
                           daily_reward=None)