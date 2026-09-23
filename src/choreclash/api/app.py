from os import getenv
from flask import Flask
from dotenv import load_dotenv

# blueprints
# from choreclash.api.routes.parent_routes import parent_bp
# from choreclash.api.routes.auth_routes import auth_bp
# from choreclash.api.routes.index_route import index_bp
# from choreclash.api.routes.chore_routes import chores_bp
# from choreclash.api.routes.child_routes import child_bp
from choreclash.api.errors.handlers import register_error_handlers

from choreclash.api.routes import (parent_routes, auth_routes, index_route,
                                   chore_routes, child_routes, reward_routes)

# Set .env efile in os.environ
load_dotenv()
secret_key = getenv("SECRET_KEY")
print(secret_key)

# Config App
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
app.register_blueprint(parent_routes.parent_bp)
app.register_blueprint(auth_routes.auth_bp)
app.register_blueprint(index_route.index_bp)
app.register_blueprint(chore_routes.chores_bp)
app.register_blueprint(child_routes.child_bp)
app.register_blueprint(reward_routes.rewards_bp)

# Register Handlers
register_error_handlers(app)

# Flask - login security
from datetime import timedelta
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=timedelta(days=7),
)






if __name__ == "__main__":
    app.run(debug=True)