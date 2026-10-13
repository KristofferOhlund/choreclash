from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service, child_service, occurence_service
from choreclash.api.helpers.helpers import get_dates_in_current_week, get_days_from_dates, get_current_week


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
    # week_dates = get_dates_in_current_week()

    # Day headers
    # header_days = get_days_from_dates(week_dates)

    # Current week (day and dates)
    week = get_current_week()

    # All chores this week
    weekly_chore_occurences = []
   
    # Chore Occurences
    if children:
        for child in children:
            # Get childs chore for current week
            childs_chore = occurence_service.get_chore_occurences(parent_id=parent_id, child_id=child.id)

            # Check if childs chores are done for the day
            # reward = 
            # occurence_service.check_daily_chores_complete(childs_chore)

            # Add chores
            weekly_chore_occurences.append({
                "child": child.id,
                "chores": childs_chore,
                "reward": None
                
            })

    # for _week in weekly_chore_occurences:
    #     for chore in _week["chores"]:
    #         print("WEEKLY CHORE", type(chore.date), chore.date)

    # for day in week:
    #     print("day in week", day["date"])

    # TODO
    # Avnänd endast week, {day, date} för att visa datum och dagar,
    # nu används header_days och week_dates
    
    # Kontrollera varje lista med chores, varje lista tillhör ett unikt barn
    # Om dagens chores är klara - erbjud reward
    
    # Problem.
    # 1. Om vi kontrollerar om samtliga uppgifter för dagen är lösta, och då erbjuder reward. Kan man få en reward varje gång man uppdaterar sidan
    #   Lösning: Om ett barn fått en reward på en dag kan den inte få flera rewards. Reward måste alltså veta datum och child som den blev erbjuden

    return render_template("dashboard.html", 
                           chores=weekly_chore_occurences, week=week, #week_dates=week, header_days=week,
                           daily_reward=None)