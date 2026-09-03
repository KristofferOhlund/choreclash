from sqlalchemy import select
from sqlalchemy.orm import Session
import choreclash.models as models
from pytest import fixture

@fixture
def session(init):
    parent = models.Parent(first_name="Kristoffer", last_name="Öhlund", email="kristoffer.ohlund@gmail.com")

    child = models.Child(first_name="Melker", parent=parent)

    with Session(init) as session:
        session.add_all([parent, child])
        session.commit()
        yield session
        session.delete(child)
        session.commit()

def test_child(session):
    child = session.scalar(select(models.Child))

    assert child.first_name == "Melker"
    assert child.id == 1
    parents = session.scalars(select(models.Parent)).all()
    assert len(parents) == 1 # make sure parent isn't created twice
    assert parents[0].id == 1

def test_child_parent_relation(session):
    child = session.scalar(select(models.Child))
    assert child.parent.first_name == "Kristoffer"

def test_empty_chore_assignment(session):
    child = session.scalar(select(models.Child))
    assert len(child.chore_assignments) == 0
    