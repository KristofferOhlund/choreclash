from choreclash.db.db import DB
from sqlalchemy.orm import Session
import choreclash.models as models
import json

# Get engine object
engine = DB()._get_engine()

# DML (Data Manipulation Language) = datan (INSERT, UPDATE, DELETE, SELECT)

# INSERT into chores_table
with Session(engine) as session:
    chore_obj = []
    with open('scripts/data/chores.json') as f:
        chores = json.load(f)
        for chore in chores:
            chore_obj.append(models.Chore(title=chore['title'], description=chore['description'], icon=chore['icon']))
    try:
        session.add_all(chore_obj)
        session.commit()
    except Exception as e:
        print(f"Error occurred while adding chore : {e}")
        session.rollback()


# INSERT into rewards_table
with Session(engine) as session:
    reward_obj = []
    with open('scripts/data/rewards.json') as f:
        data = json.load(f)
        for reward in data["rewards"]:
            reward_obj.append(models.Reward(title=reward['title'], description=reward['description'], reward_type=reward["reward_type"], icon=reward['icon']))
    try:
        session.add_all(reward_obj)
        session.commit()
    except Exception as e:
        print(f"Error occurred while adding reward : {e}")
        session.rollback()
