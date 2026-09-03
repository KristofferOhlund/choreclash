from sqlalchemy import select
from sqlalchemy.orm import Session
import choreclash.models as models
from pytest import fixture

@fixture
def session(init):
    parent = models.Parent(first_name="Kristoffer", last_name="Öhlund", email="kristoffer.ohlund@gmail.com")

    with Session(init) as session:
        session.add(parent)
        session.commit()
        yield session
        session.delete(parent)
        session.commit()

def test_parent(session):
    # Assert
    parent = session.scalar(select(models.Parent))

    assert parent.first_name == "Kristoffer"
    assert parent.id == 1

def test_relationship_empty(session):
    parent = session.scalar(select(models.Parent))

    assert len(parent.children) == 0

def test_relationship_one(session):
    parent = session.scalar(select(models.Parent))

    child = models.Child(first_name="Melker")

    parent.children.append(child)

    # session.add(child)
    session.flush()

    # Make sure db is updated
    parent = session.scalar(select(models.Parent))

    assert len(parent.children) == 1
    
    child = session.scalar(
    select(models.Child)
    .where(
        models.Child.id == child.id,
        models.Child.parent_id == parent.id
    ))

    assert child.parent.id == parent.id
