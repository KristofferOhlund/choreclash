from choreclash.db.db import Base, DB
from sqlalchemy.orm import Session
from choreclash.models.chore_template import ChoreTemplate
from choreclash.models.chore_assignment import ChoreAssignment
from choreclash.models.parent import Parent
from choreclash.models.children import Child

# Get engine object
engine = DB().get_engine()


# DML (Data Manipulation Language) = datan (INSERT, UPDATE, DELETE, SELECT)

## INSERT into chore_template_table
with Session(engine) as session:
    # Insert a new parent
    new_parent = Parent(
        first_name="John",
        last_name="Doe",
        email="John.Doe@sample.com")

    # Insert new child
    new_child = Child(
        first_name="Jane",
        parent_id=new_parent.id
    )

    # Insert a new chore template
    new_chore_template = ChoreTemplate(
        parent_id=None,
        title="Clean Room",
        icon="clean_icon.png",
        description="Clean your room thoroughly.",
        is_complete=False,
        deadline=None
    )

    # insert a new chore assignment
    new_chore_assignment = ChoreAssignment(
        child_id=new_child.id,
        chore_template_id=new_chore_template.id
    )

    session.add(new_parent)
    session.add(new_child)
    session.add(new_chore_template)
    session.add(new_chore_assignment)

    session.commit()

    # Query all chore templates
    parent = session.query(Parent).first()
    for chore in parent.children.chores:
        print(chore.get_title(), chore.get_description(), chore.get_parent_id())
