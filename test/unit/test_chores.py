from sqlalchemy import select
from sqlalchemy.orm import Session
import choreclash.models as models
from pytest import fixture

@fixture
def session(init):
    chore = models.Chore(title="Städa rummet", description="Städa rummet noggrant")

    with Session(init) as session:
        session.add(chore)
        session.commit()
        yield session
        session.delete(chore)
        session.commit()

def test_chore(session):
    chore = session.scalar(select(models.Chore))

    assert chore.title == "Städa rummet"
    assert chore.id == 1
    assert len(chore.child_assignments) == 0

