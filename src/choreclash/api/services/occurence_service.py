"""
ChoreOccurence module service to handle ChoreOccurences
"""
from flask import session
from choreclash.models import Chore2Child, ChoreOccurence
from datetime import datetime
from choreclash.api.helpers.string_helper import create_list_from_string, format_dates

from choreclash.db.db import DB

def create_chore_occurence(chore2child: list[Chore2Child], dates:list[datetime]):
    """
    For each Chore2Child object, create ChoreOccurence from date

    Args:
        chore2child: list of Chore2Child objects
        dates: list of dates as datetime objects
    """
    
    list_of_dates = create_list_from_string(dates)
    datetime_dates = format_dates(list_of_dates)

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