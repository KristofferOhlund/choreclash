from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import choreclash.models as models

def test_parent():
    engine = create_engine("sqlite:///test.db", echo=True)
    models.Base.metadata.create_all(engine)

    with Session(engine) as session:
        children = models.Child(
            first_name="Jane",
            parent_id=1,
        )

        try:
            session.add(children)
            session.commit()
        except Exception as e:
            print(f"Error occurred while adding child: {e}")
            session.rollback()

        retrieved_children = session.get(models.Child, children.id)

        assert retrieved_children is not None
        assert retrieved_children.first_name == "Jane"