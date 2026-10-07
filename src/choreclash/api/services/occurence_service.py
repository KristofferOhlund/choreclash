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


def get_chore_occurences_by_week(parent_id : str, week_number : str = None):
    """
    Return all chores based on week number and parent id

    Params:
        parent_id: str: the ID of the parent
        week_number: str: week number as string

    Returns:
        List of ChoreOccurence objects, including relationships (eager loading)
    """

    # Default week_number
    if week_number is None:
        week_number = datetime.today().isocalendar().week

    # Date ranges in week_number
    dates = helpers.get_dates_in_current_week()
    monday, sunday = min(dates), max(dates)

    db = DB()
    with db.get_session() as session:
        occurences = session.scalars(select(ChoreOccurence)
                .options(
                selectinload(ChoreOccurence.assignment)
                .selectinload(Chore2Child.chore),
                selectinload(ChoreOccurence.assignment)
                .selectinload(Chore2Child.child))).all()
        # .where(
        #     Parent.id == parent_id,
        #     ChoreOccurence.date >= monday,
        #     ChoreOccurence.date <= sunday
        #     )
        #     ).all()

        return occurences


def toggle_chore_occurence(occurence_id : str = None, parent_id: str = None):
    """
    Toggle a chore occurence based on occurence and parent ID
    """
    db = DB()
    with db.get_session() as db_session:
        occurence = db_session.scalar(select(ChoreOccurence).where(
            ChoreOccurence.id == occurence_id,
            Parent.id == parent_id
            ))
        try:
            if occurence.is_complete:
                occurence.is_complete = False
            else:
                occurence.is_complete = True

            db_session.add(occurence)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            return("something went wrong", e)


def get_occurences_by_date(date: str, child_id: str):
    """
    Return all on specific date, by child id
    """
    db = DB()
    with db.get_session() as db_session:
        occurences = db_session.scalars(select(ChoreOccurence).where(
            ChoreOccurence.date == date,
            Child.id == child_id
            ))
        return occurences


# {def check_daily_chores_complete(dates: list) -> list: 
#     """
#     Return list of days where chores are complete.
#     If all chores on monday are complete, return [Monday]
#     If all chores for Monday and Thursday are complete, return ["Monday", "Thursday"]
#     """
#     days = {}
#     for date in dates:
#         # get chores by date
#         occurences = get_occurences_by_date(date)
#         if all(lambda x: x.is_complete for x in occurences):
#             days["child"] = 
                    

#     return days
# }
