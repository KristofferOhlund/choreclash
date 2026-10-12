"""
ChoreOccurence module service to handle ChoreOccurences
"""
from flask import session
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from choreclash.models import Chore2Child, ChoreOccurence, Parent, Child
from datetime import datetime
from choreclash.api.helpers import helpers
from choreclash.db.db import DB

def create_chore_occurence(chore2child: list[Chore2Child], dates:list[datetime]):
    """
    For each Chore2Child object, create ChoreOccurence from date

    Args:
        chore2child: list of Chore2Child objects
        dates: list of dates as datetime objects
    """
    
    list_of_dates = helpers.create_list_from_string(dates)
    datetime_dates = helpers.format_dates(list_of_dates)

    db = DB()
    try:
        with db.get_session() as session:
            for c2c in chore2child:
                for date in datetime_dates:
                    occurence = ChoreOccurence(date=date, assignment=c2c)
                    session.add(occurence)
            session.commit()
    except Exception as e:
        print(f"Error creating chore2child: {e}")
        session.rollback()


def get_chore_occurences(parent_id : int, child_id : int = None, start_date : datetime = None, end_date : datetime = None)-> list[ChoreOccurence]:
    """
    Return a list of ChoreOccurence.
    If child_id, filters occurences based on child id, defaults to None. If not child_id, returns all ChoreOccurences.
    Start and end date are optional, defaults to None
    
    Params:
        parent_id: int: The ID of a parent
        child_id: int: The ID of a child, defaults to None
        start_date: optional, if start date, returns occurence >= to start_date
        end_date: optional, if start date, returns occurence <= to start_date
    
    Returns:
        list[ChoreOccurence]: list of ChoreOccurences
    """

    # Default start date
    if not start_date:
        start_date = min(helpers.get_dates_in_current_week())

    if not end_date:
        end_date = max(helpers.get_dates_in_current_week())

    db = DB()
    with db.get_session() as session:
        occurences = session.scalars(select(ChoreOccurence)
                .join(ChoreOccurence.assignment)
                .join(Chore2Child.child)
                .options(
                selectinload(ChoreOccurence.assignment)
                .selectinload(Chore2Child.chore),
                selectinload(ChoreOccurence.assignment)
                .selectinload(Chore2Child.child))
        .where(
            Parent.id == parent_id,
            Child.id == child_id,
            ChoreOccurence.date >= start_date,
            ChoreOccurence.date <= end_date
            )
            ).all()

        return occurences


def complete_chore_occurence(occurence_id : str = None, parent_id: str = None)-> None:
    """
    Complete a chore occurence based on occurence and parent ID
    Only chores with todays date can be completed.

    Params:
        occurence_id: str: the ID of a ChoreOccurence
        parent_id: str: the ID of a Parent
    """

    db = DB()
    with db.get_session() as db_session:
        occurence = db_session.scalar(select(ChoreOccurence).where(
            ChoreOccurence.id == occurence_id,
            Parent.id == parent_id
            ))
        try:
            today = helpers.format_date(datetime.today())
            oc_date = helpers.format_date(occurence.date)
            if today == oc_date:
                occurence.is_complete = True
            db_session.add(occurence)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            return("something went wrong", e)

def check_daily_chores_complete(chores: list[ChoreOccurence]) -> list[str]: 
    """
    Return list of days where chores are complete.
    If all chores on monday are complete, return [Monday]
    If all chores for Monday and Thursday are complete, return ["Monday", "Thursday"]
    """

    raise NotImplementedError
    days = {
        "Måndag": {
            "chores": [],
            "chores_complete" : False
        },
        "Tisdag": {
            "chores": [],
            "chores_complete" : False
        },
        "Onsdag": {
            "chores": [],
            "chores_complete" : False
        },
        "Torsdag": {
            "chores": [],
            "chores_complete" : False
        },
        "Fredag": {
            "chores": [],
            "chores_complete" : False
        },
        "Lördag": {
            "chores": [],
            "chores_complete" : False
        },
        "Södag": {
            "chores": [],
            "chores_complete" : False
        },
        
    }

    # Split chores by day
    for chore in chores:
        swedish_day = helpers.get_swedish_day(chore.date.strftime("%A"))
        days[swedish_day].chores.append(chore)

    for day in days:
        if all(chore.is_complete for chore in day["chores"]):
            day["chores_complete"] = True
            # reward_service skapar reward objecct
            # child id, chore id, date

    return days
