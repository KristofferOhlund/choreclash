from flask import Blueprint, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import Session

from choreclash.db.db import DB
from choreclash.models.parent import Parent


parent_bp = Blueprint(
    "parents",
    __name__,
    url_prefix="/api/parents"
)

db = DB()

### GET ###

@parent_bp.get("/")
def get_parents():
    with db.get_session() as session:
        parents = session.scalars(
            select(Parent)
        ).all()

        return jsonify([
            {
                "id": parent.id,
                "first_name": parent.first_name,
                "last_name": parent.last_name,
                "email": parent.email
            }
            for parent in parents
        ])



@parent_bp.get("/<int:parent_id>")
def get_parent_with_id(parent_id):
    with Session(engine) as session:
        parents = session.scalars(
            select(Parent)
        ).all()

        return jsonify([
            {
                "id": parent.id,
                "first_name": parent.first_name,
                "last_name": parent.last_name,
                "email": parent.email
            }
            for parent in parents
        ])


@parent_bp.post("/")
def create_parent():
    data = request.get_json()

    parent = Parent(
        first_name=data["first_name"],
        last_name=data["last_name"],
        avatar_url=data.get("avatar_url"),
        email=data["email"],
        password_hash=data.get("password_hash")
    )

    with Session(engine) as session:
        session.add(parent)
        session.commit()

        return jsonify({
            "id": parent.id,
            "first_name": parent.first_name,
            "last_name": parent.last_name,
            "email": parent.email
        }), 201