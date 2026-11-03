"""
Reward service module for managing rewards.
"""
from sqlalchemy import select, func
from choreclash.models.reward import Reward, Reward2Child, RewardOccurrence
from choreclash.models.children import Child
from choreclash.db.db import DB
from random import randint
from flask import jsonify
from datetime import datetime


def get_reward(reward_id: str):
    """
    Get a reward by its ID.

    Args:
        reward_id (str): The ID of the reward to be retrieved.
    """
    db = DB()
    with db.get_session() as db_session:
        try:
            reward = db_session.scalar(select(Reward).where(Reward.id == reward_id))
            return reward
        except Exception as e:
            db_session.rollback()
            return f"Could not fetch a reward using reward id {reward_id} \\n Error. {e}"

def get_rewards():
    """
    Retrieve all rewards.

    Returns:
        list: A list of reward objects
    """
    db = DB()
    with db.get_session() as db_session:
        rewards = db_session.query(Reward).all()
        return rewards

def update_reward(reward_id: str, updated_data: dict):
    """
    Update a reward

    Args:
        reward_id (str): The ID of the reward to be updated.
        updated_data (dict): A dictionary containing the updated reward data.
    """
    db = DB()
    with db.get_session() as db_session:
        reward = db_session.query(reward).filter_by(id=reward_id).first()
        if reward:
            for key, value in updated_data.items():
                setattr(reward, key, value)
            db_session.commit()

def delete_reward(reward_id: str):
    """
    Delete a reward

    Args:
        reward_id (str): The ID of the reward to be deleted.
    """
    db = DB()
    with db.get_session() as db_session:
        reward = db_session.query(reward).filter_by(id=reward_id).first()
        if reward:
            db_session.delete(reward)
            db_session.commit()

def create_reward(reward_data: dict):
    """
    Create a new reward

    Args:
        reward_data (dict): A dictionary containing the reward data.
    """
    db = DB()
    try:
        with db.get_session() as db_session:
            new_reward = Reward(**reward_data)
            db_session.add(new_reward)
            db_session.commit()
    except Exception as e:
        print(f"Error creating reward: {e}")
        db_session.rollback()

def roll_reward()-> Reward:
    """
    Roll reward
    """
    rewards_in_db = get_rewards()
    if rewards_in_db:
        return rewards_in_db[randint(a=0, b=len(rewards_in_db) -1)]

def assign_reward(child_object: Child = None, reward_id: int = None):
    """
    Assign a reward to child, only if the child has not already recieved a reward for that today

    Params:
        child_id: int: the child with ID to assign a reward to
        reward_id: int: Fetch reward with id == id and assign to child
    """
    db = DB()
    with db.get_session() as db_session:
        has_reward = db_session.scalar(
            select(RewardOccurrence)
            .join(RewardOccurrence.assignment)
            .join(Reward2Child.child)
            .where(
                Child.id == child_object.id,
                func.date(RewardOccurrence.assigned_at) == datetime.today().date()
            )
        )
        # Child has not recieved a reward for today
        if has_reward is None:
                reward = get_reward(reward_id=reward_id)
                reward2child = Reward2Child(child=child_object, reward=reward)
                occurrence = RewardOccurrence(assignment=reward2child)
                try:
                    db_session.add(occurrence)
                    db_session.commit()
                except Exception as e:
                    db_session.rollback()
                    return f"Something went wrong when creating a new RewardOccurence"
