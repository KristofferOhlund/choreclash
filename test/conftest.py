import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import choreclash.models as models

@pytest.fixture
def setup_database():
    engine = create_engine("sqlite:///:memory:", echo=True, future=True)
    models.Base.metadata.create_all(engine)
    yield engine
    models.Base.metadata.drop_all(engine)

@pytest.fixture
def init(setup_database):
    engine = setup_database
    with Session(engine) as session:
        parent = models.Parent(
            first_name="Anna",
            last_name="Andersson",
            email="anna@example.com"
        )
        child = models.Child(id=1, first_name="Lisa", parent=parent)
        chore1 = models.Chore(title="Städa toaletten", description="Städa rummet noggrant", icon="room_icon.png")
        chore2 = models.Chore(title="Packa väskan", description="Paska väskan inför skolan", icon="väska_icon.png")

        chore2child1 = models.Chore2Child(
            child=child,
            chore=chore1
        )

        chore2child2 = models.Chore2Child(
            child=child,
            chore=chore2
        )

        session.add_all([chore2child1, chore2child2])
        session.commit()

    return engine