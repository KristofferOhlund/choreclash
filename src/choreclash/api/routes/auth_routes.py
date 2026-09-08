from flask import Blueprint, render_template, request

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # hantera login
        pass

    return render_template("login.html")

@auth_bp.route("/register")
def register():
    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    return render_template("logout.html")

