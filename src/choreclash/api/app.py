from flask import Flask

# blueprints
from choreclash.api.routes.parent_routes import parent_bp
from choreclash.api.routes.auth_routes import auth_bp
from choreclash.api.errors.handlers import register_error_handlers

app = Flask(__name__)
app.register_blueprint(parent_bp)
app.register_blueprint(auth_bp)
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