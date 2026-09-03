import pytest
from sqlalchemy import create_engine
import choreclash.models as models

@pytest.fixture
def setup_database():
    # engine = create_engine("sqlite:///test.db")
    engine = create_engine("sqlite:///:memory:", echo=True, future=True)
    models.Base.metadata.create_all(engine)
    yield engine
    models.Base.metadata.drop_all(engine)

@pytest.fixture
def init(setup_database):
    engine = setup_database
    return engine