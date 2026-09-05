from flask import Flask, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import Session

from choreclash.db.db import DB
from choreclash.models.parent import Parent
from choreclash.models.children import Child
from choreclash.models.chores import Chore
from choreclash.models.chore2child import Chore2Child


from choreclash.api.routes.parent_routes import parent_bp


app = Flask(__name__)
app.register_blueprint(parent_bp)





if __name__ == "__main__":
    app.run(debug=True)