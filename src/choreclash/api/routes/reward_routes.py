from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session, jsonify)

from choreclash.db.db import DB
from choreclash.api.services import (
    reward_service, child_service)


rewards_bp = Blueprint(
    "rewards",
    __name__,
)

db = DB()

@rewards_bp.route("/rewards", methods=["GET"])
def rewards():
    parent_id = session.get("parent_id")
    if not parent_id:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("auth.login"))

    # get all rewards in db  
    rewards = reward_service.get_rewards()

    return render_template("rewards.html", rewards=rewards)

# @rewards_bp.route("/rewards/<int:chore_id>/edit", methods=["GET", "POST"])
# def edit(chore_id):
#     parent_id = session.get("parent_id")
#     if not parent_id:
#         flash("You must be logged in to access this page.", "error")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         reward_service.update_chore(chore_id, request.form)
#         flash("Chore updated successfully.", "success")
#         return redirect(url_for("rewards.rewards"))

#     chore = reward_service.get_chore(chore_id)
#     return render_template("edit_chore.html", chore=chore)

@rewards_bp.route("/rewards/create", methods=["GET", "POST"])
def create():
    parent_id = session.get("parent_id")
    if not parent_id:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        reward_service.create_reward(request.form)
        flash("Reward created successfully.", "success")
        return redirect(url_for("rewards.rewards"))

    return render_template("create_reward.html")


# @rewards_bp.route("/rewards/<int:chore_id>/delete", methods=["POST"])
# def delete(chore_id):
#     parent_id = session.get("parent_id")
#     if not parent_id:
#         flash("You must be logged in to access this page.", "error")
#         return redirect(url_for("auth.login"))

#     reward_service.delete_chore(chore_id)
#     flash("Chore deleted successfully.", "success")
#     return redirect(url_for("rewards.rewards"))


@rewards_bp.route("/rewards/assign", methods=["POST"])
def assign():
    parent_id = session.get("parent_id")
    if not parent_id:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("auth.login"))

    child_id = request.form.get("child_id", type=int)
    reward_id = request.form.get("reward_id", type=int)

    if child_id and reward_id:
        # get child object
        child = child_service.get_child(parent_id=parent_id, child_id=child_id)
        
        reward_service.assign_reward(child_object=child, reward_id=reward_id)

    return redirect(url_for("dashboard.dashboard"))