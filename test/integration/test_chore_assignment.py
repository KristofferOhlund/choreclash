from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from choreclash.db.db import Base
from choreclash.models.parent import Parent
from choreclash.models.children import Child
from choreclash.models.chore_template import ChoreTemplate
from choreclash.models.chore_assignment import ChoreAssignment


def test_create_chore_assignment():
    engine = create_engine("sqlite:///test.db", echo=True, future=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        parent = Parent(
            first_name="Anna",
            last_name="Andersson",
            email="anna@example.com",
        )
        child = Child(first_name="Lisa", parent=parent)
        chore = ChoreTemplate(title="Städa rummet", parent=parent)

        assignment = ChoreAssignment(
            child=child,
            chore_template=chore,
        )

        session.add(assignment)
        session.commit()

        assert assignment.id is not None
        assert assignment.child_id == child.id
        assert assignment.chore_template_id == chore.id

