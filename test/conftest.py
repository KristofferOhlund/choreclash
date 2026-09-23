import pytest
from sqlalchemy import create_engine
import choreclash.models as models

@pytest.fixture
def init():
    engine = create_engine("sqlite:///test.db", echo=True, future=True)
    models.Base.metadata.create_all(engine)
    yield engine
    models.Base.metadata.drop_all(engine)
