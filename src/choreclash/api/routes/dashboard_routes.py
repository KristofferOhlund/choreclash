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

    # All children of parent
    children = child_service.get_children(parent_id=parent_id)
    
    # Current Week dates
    week_dates = get_dates_in_current_week()

    # Day headers
    header_days = get_days_from_dates(week_dates)
   
    # Chore Occurences
    if children:
        weekly_chore_occurences = []
        for child in children:
            weekly_chore_occurences.extend(occurence_service.get_chore_occurences(parent_id=parent_id, child_id=child.id))

    # Kontrollera om kids samtliga dagliga occurence är klara

    # Hämta istället weekly_chore_occurence_by_child_id
    # då blir det lätt att kontrollera respektive barns uppgifter
    # Det svåra blir att loopa genom barnen, vi vet inte hur många barn

    # Vi har alla veckans chores

    # Vi behöver kolla om person x uppgifter för dag y är klara
    # - dela veckans uppgifter per barn
    # - kontrollera varje dag som barnet har uppgifter för

    # Split chores by child

    return render_template("dashboard.html", 
                           chores=weekly_chore_occurences, week_dates=week_dates, header_days=header_days,
                           daily_reward=None)