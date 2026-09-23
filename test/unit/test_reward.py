from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select
import choreclash.models as models
from pytest import fixture


def test_reward_create(init):
    reward = models.Reward(title="skärmtid", description="20 min mer skärmtid", reward_type="daily")
    with Session(init) as session:
        session.add(reward)
        session.flush()
        assert reward.id is 1

def test_reward2child_create(init):
    reward2Child = models.Reward2Child(child_id=1, reward_id=1)

    with Session(init) as session:
        session.add(reward2Child)
        session.flush()
        assert reward2Child.id == 1

def test_reward_occurence_create(init):
    occurence = models.RewardOccurence(reward_2_child_id=1)

    with Session(init) as session:
        session.add(occurence)
        session.flush()
        assert occurence.id == 1
        assert occurence.used == False




        

