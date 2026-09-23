"""
Reward service module for managing rewards.
"""
from flask import session
from choreclash.models.reward import Reward
from choreclash.db.db import DB


def get_reward(reward_id: str):
    """
    Get a reward by its ID.

    Args:
        reward_id (str): The ID of the reward to be retrieved.
    """
    db = DB()
    with db.get_session() as db_session:
        reward = db_session.query(reward).filter_by(id=reward_id).first()
        return reward

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
            new_reward = reward(**reward_data)
            db_session.add(new_reward)
            db_session.commit()
    except Exception as e:
        print(f"Error creating reward: {e}")
        session.rollback()