import regex as re

def validate_email(email:str) -> bool:
    """
    Validates Email

    Args: email: email adress to be validated

    Returns: True if valid

    Raises: ValueError if email does not match regex 
    """

    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email_match = re.match(email_pattern, email)

    if not email_match:
        raise ValueError("Vänlig ange en giltig e-post")

def validate_passwords(pass1:str, pass2:str) -> bool:
    """
    Validate password

    - Have at least one number
    - Have at least one uppercase letter
    - Have at least one lowercase letter
    - Have at least one special character ($, @, #, %)
    - Have a minumum of 12 characters
    
    Args: pass1: The first password. pass2: The second password. 

    Returns: True if both passwords are valid and match. 
    
    Raises: 
        ValueError: If the passwords do not match. 
        ValueError: If the password does not meet the requirements.
    """
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{12,}$"

    if not pass1 == pass2:
        raise ValueError("Lösenorden matchar inte")

    password_match = re.match(password_pattern, pass1)
    if not password_match:
        raise ValueError(
            "Lösenordet måste innehålla minst 12 tecken, "
            "en stor bokstav, en liten bokstav, en siffra "
            "och ett specialtecken (@, $, # eller %)."
        )

    return True


def validate_string(input_string:str, field_name:str) -> bool:
    """
    Validate string input

    Args: input_string: The string to be validated. field_name: The name of the field.

    Returns: True if the string is valid.

    Raises: ValueError if the string is empty or contains only whitespace.
    """
    if not input_string or input_string.strip() == "":
        raise ValueError(f"{field_name} får inte vara tomt.")

    return True


if __name__ == "__main__":
    validate_email("kristoffer.ohlund@icloud.com")
    validate_string("John", "First name")
    validate_string("Doe", "Last name")