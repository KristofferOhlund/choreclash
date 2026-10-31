"""
Tests to Test that a Reward can be assigned to a Child
"""

import choreclash.models as models
from pytest import fixture
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select

@fixture
def init_assignment(init):
    """
    Inits a reward assignement where a Reward is assigned to a Child

    Params:
        init: sqlAclchemy engine

    Returns:
        Session object
    """
    # We first create the Child object to be recieve the Reward
    parent = models.Parent(first_name="Kristoffer", last_name="Öhlund", email="kristoffer.ohlund@gmail.com")
    child = models.Child(first_name="Melker", parent=parent)

    # Create reward to be assigned
    reward = models.Reward(title="Välj film", description="Du får välja kvällens film", reward_type="daily")
    
    reward2Child = models.Reward2Child(child=child, reward=reward)
    # add occurence
    occurrence = models.RewardOccurrence(assignment=reward2Child)
    
    with Session(init) as session:
        session.add(occurrence)
        session.flush()

        yield session


def test_reward_creation(init_assignment):
    """
    Test that 1 reward has been created
    """
    res = init_assignment.scalars(select(models.Child)).all()

    assert len(res[0].reward_assignments) == 1

def test_reward_relation(init_assignment):
    """
    Test that reward has been created with the correct Title
    """
    res = init_assignment.scalar(select(models.Child))

    assert res.reward_assignments[0].reward.title == "Välj film"

def test_reward2child_child_relation(init_assignment):
    """
    Test that reward was assigned to the correct child
    """
    res = init_assignment.scalar(select(models.Child))

    assert res.reward_assignments[0].child.first_name == "Melker"

def test_occurences_count(init_assignment):
    """
    Test reward occurrences count
    """
    res = init_assignment.scalar(select(models.Child))

    assert len(res.reward_assignments[0].occurrences) == 1

def test_reward_occurences_assignment_relation(init_assignment):
    """
    Test the relation between RewardOccurrences and Reward2Child
    """
    res = init_assignment.scalar(select(models.Child))

    assert res.reward_assignments[0].occurrences[0].assignment.id == 1

def test_reward_occurences_assigned_at(init_assignment):
    """
    Test that assigned_at == datetime.today.date
    """
    res = init_assignment.scalar(select(models.Child))
    occurrence = res.reward_assignments[0].occurrences[0]

    assert occurrence.assigned_at.date() == datetime.today().date()
    
def test_reward_occurence_is_not_used(init_assignment):
    """
    Test reward occurrence used property is False by default
    """
    res = init_assignment.scalar(select(models.Child))

    assert res.reward_assignments[0].occurrences[0].used == False

def test_reward_occurence_is_used(init_assignment):
    """
    Test reward occurrence used property is False by default
    """
    res = init_assignment.scalar(select(models.Child))

    occurrence = res.reward_assignments[0].occurrences[0]
    occurrence.used = True
    init_assignment.flush()
    # Add -s flag to show output
    print("used_at:", occurrence.used_at)
    print("type:", type(occurrence.used_at))
    print(datetime.today().date())
    assert res.reward_assignments[0].occurrences[0].used == True
    assert res.reward_assignments[0].occurrences[0].used_at.date() == datetime.today().date()



