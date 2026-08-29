from sqlalchemy import select
from sqlalchemy.orm import Session
import choreclash.models as models

# def test_chore2child_relationship(init):
#     engine = init
#     with Session(engine) as session:
#         chore2child = session.execute(select(models.Chore2Child)).scalar()
        
#         assert len(chore2child) == 2


def test_chore2child_count(init):
    engine = init
    with Session(engine) as session:
        chore2child = session.execute(select(models.Chore2Child)).scalars().all()
        
        assert len(chore2child) == 2

def test_add_chore2child(init):
    engine = init
    with Session(engine) as session:
        parent = session.execute(select(models.Parent)).scalar()
        child = models.Child(id=2, first_name="Krille", parent=parent)
        chore = models.Chore(title="Ta på kläder", description="Ta på kläder inför skolan")
        chore2child = models.Chore2Child(child=child, chore=chore)

        session.add(chore2child)
        session.commit()

        # Make sure it was created
        chore2child = session.execute(select(models.Chore2Child)).scalars().all()
        assert len(chore2child) == 3

        created_chore2child = session.scalar(select(models.Chore2Child).where(models.Child.id == child.id))

        assert isinstance(created_chore2child, models.Chore2Child)
        