from sqlalchemy import select
from sqlalchemy.orm import Session
import choreclash.models as models
from pytest import fixture

@fixture
def session(init):
    parent = models.Parent(first_name="Kristoffer", last_name="Öhlund", email="kristoffer.ohlund@icloud.com")

    child = models.Child(first_name="Melker", parent=parent)

    chore = models.Chore(title="Städa rummet")

    chore2child = models.Chore2Child(child=child, chore=chore)

    occurence = models.ChoreOccurence(assignment=chore2child)

    with Session(init) as session:
        session.add(occurence)
        session.commit()

    return session

def test_chore_creation(session):
    chore = session.scalar(select(models.Chore))

    assert chore.title == "Städa rummet"
    assert chore.id == 1
    ## Child is assigned a chore because of chore2child, but occurences are not set
    assert len(chore.child_assignments) == 1

def test_child_creation(session):
    child = session.scalar(select(models.Child))

    assert child.first_name == "Melker"
    assert child.id == 1

def test_parent_creation(session):
    parent = session.scalars(select(models.Parent)).all()

    assert len(parent) == 1

def test_chore_occurence_empty(session):
    occurence = session.scalar(select(models.ChoreOccurence))

    assert occurence is not None
    assert occurence.is_complete == False
    assert occurence.assignment.chore.id == 1
    assert occurence.assignment.child.id == 1

