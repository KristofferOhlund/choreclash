from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import choreclash.models as models

def test_parent():
    engine = create_engine("sqlite:///test.db", echo=True)
    models.Base.metadata.create_all(engine)

    with Session(engine) as session:
        chore = models.Chore(
            title="Test Chore",
            description="This is a test chore."
        )
        try:
            session.add(chore)
            session.commit()
        except Exception as e:
            print(f"Error occurred while adding chore: {e}")
            session.rollback()

        retrieved_chore = session.get(models.Chore, chore.id)

        assert retrieved_chore is not None
        assert retrieved_chore.title == "Test Chore"
        assert retrieved_chore.description == "This is a test chore."