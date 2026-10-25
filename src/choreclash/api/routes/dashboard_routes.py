from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.api.services import parent_service, child_service, occurence_service, reward_service
from choreclash.api.helpers.helpers import get_dates_in_current_week, get_days_from_dates, get_current_week, get_todays_date


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
)

db = DB()

@dashboard_bp.route("/dashboard/", methods=["GET"])
def dashboard():
    """
    Show all children chores

    Query Param:
        assign_reward_to: int: assign a reward to child with id, defaults to None
    """
    parent_id = session.get("parent_id")
    if not parent_id:
        return redirect("auth.login")

    # All children of parent
    children = child_service.get_children(parent_id=parent_id)
    
    # Current week (day and dates)
    week = get_current_week()

    # Today - don't redirect unless today
    today = get_todays_date()

    # All chores for a child have been completed
    # Therefore assigns a reward to that child
    assign_reward_to_child = request.args.get("assign_reward_to", type=int)
    if assign_reward_to_child:
        reward = reward_service.roll_reward()
        reward_service.assign_reward(child_id=assign_reward_to_child, reward=reward)

    # All chores this week to display
    weekly_chore_occurences = []

    # Chore Occurences
    if children:
        for child in children:
            # Get childs chore for current week
            childs_chore = occurence_service.get_chore_occurences(parent_id=parent_id, child_id=child.id)

            # Add chores
            weekly_chore_occurences.append({
                "child": child,
                "chores": childs_chore,
            })


    return render_template("dashboard.html", 
                           children_chores=weekly_chore_occurences, week=week, today=today, reward_offer=None)