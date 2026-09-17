





from datetime import datetime

print()

def create_list_from_string(string) -> list:
    """
    Create a list from a string where the string is a comma-separated list of items.

    Args:
        string (str): The input string. ["one, two, tree"]

    Returns:
        list: A list of items extracted from the string. ["one", "two", "tree"]
    """

    return ",".join([item.replace(" ", "") for item in string]).split(",")


def format_dates(dates:list) -> datetime:
    """
    Format a list of date strings into datetime objects. 

    Args:
        dates (list): A list of date strings in the format "YYYY-MM-DD".

    Returns:
        list: A list of datetime objects.
    """
    return [datetime.strptime(date, "%Y-%m-%d") for date in dates]
