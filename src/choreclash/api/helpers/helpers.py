from datetime import datetime, date, timedelta

DAYS = {
    "Monday": "Måndag",
    "Tuesday": "Tisdag",
    "Wednesday": "Onsdag",
    "Thursday": "Torsdag",
    "Friday": "Fredag",
    "Saturday": "Lördag",
    "Sunday": "Söndag",
}

def create_list_from_string(string) -> list:
    """
    Create a list from a string where the string is a comma-separated list of items.

    Args:
        string (str): The input string. ["one, two, tree"]

    Returns:
        list: A list of items extracted from the string. ["one", "two", "tree"]
    """

    return ",".join([item.replace(" ", "") for item in string]).split(",")


def format_dates(dates:list) -> date:
    """
    Format a list of date strings into date objects. 

    Args:
        dates (list): A list of date strings in the format "YYYY-MM-DD".

    Returns:
        list: A list of date objects.
    """
    return [datetime.strptime(date, "%Y-%m-%d").date() for date in dates]


def get_dates_in_current_week():
    """
    Get all dates in current week.

    Returns:
        list of datetime.date objects
    """
    today = date.today()
    monday = today - timedelta(days=today.weekday())

    # Get list of datetime.date objects
    return [
        monday + timedelta(days=i)
        for i in range(7)
    ]

def get_days_from_dates(dates: list):
    """
    Get the swedish names of days from a list of datetime dates

    Params:
        dates: list: list of datetime.dates objects

    Returns:
        list: list of days name in Swedish
    """
    return [
        DAYS[date.strftime("%A")] for date in dates
    ]

def get_day_from_date(value: date):
    """
    Return the swedish name for a day, based on date

    Params:
        date: datetime.date object

    Returns:
        day: str: day of name in Swedish
    """
    if not isinstance(value, date):
        raise ValueError(f"Date has to be datetime.date object, recieved {type(date)}")
    return DAYS[value.strftime("%A")]


def get_current_week_number():
    """
    Return the current week as int
    """
    return date.today().isocalendar().week

def get_current_week_day():
    """
    Return the number of current day as int, monday = 0, sunday = 6 
    """