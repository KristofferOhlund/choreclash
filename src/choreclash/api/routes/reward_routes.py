from flask import (
    Blueprint, redirect, render_template, request, flash, url_for, session)

from choreclash.db.db import DB
from choreclash.api.services import (
    reward_service, parent_service, chore2child_service, occurence_service)


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

# @rewards_bp.route("/rewards/create", methods=["GET", "POST"])
# def create():
#     parent_id = session.get("parent_id")
#     if not parent_id:
#         flash("You must be logged in to access this page.", "error")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         reward_service.create_chore(request.form)
#         flash("Chore created successfully.", "success")
#         return redirect(url_for("rewards.rewards"))

#     return render_template("create_chore.html")


# @rewards_bp.route("/rewards/<int:chore_id>/delete", methods=["POST"])
# def delete(chore_id):
#     parent_id = session.get("parent_id")
#     if not parent_id:
#         flash("You must be logged in to access this page.", "error")
#         return redirect(url_for("auth.login"))

#     reward_service.delete_chore(chore_id)
#     flash("Chore deleted successfully.", "success")
#     return redirect(url_for("rewards.rewards"))


# @rewards_bp.route("/rewards/assign", methods=["GET", "POST"])
# def assign():
#     parent_id = session.get("parent_id")
#     if not parent_id:
#         flash("You must be logged in to access this page.", "error")
#         return redirect(url_for("auth.login"))

#     children = parent_service.get_children(parent_id)
#     rewards = reward_service.get_rewards()

#     if request.method == "POST":
#         child_ids = request.form.getlist("child_id")
#         chore_ids = request.form.getlist("chore_id")
#         c2c_objects = chore2child_service.create_chore2child(child_ids=child_ids, chore_ids=chore_ids)
#         dates = request.form.getlist("dates")
#         occurence_service.create_chore_occurence(chore2child=c2c_objects, dates=dates)
#         flash("Chore assigned successfully.", "success")
#         return redirect(url_for("rewards.rewards"))

#     return render_template("chore2child.html", rewards=chores, children=children)

