import doctest
import re


def password_validator(user_password: str):
    """A function to validate the user's entered password.

    >>> password_validator("AAb88cc030")
    True
    >>> password_validator("aaaa")
    False
    >>> password_validator("984bhgbf")
    False
    >>> password_validator("")
    False"""
    password_length = re.compile(r".{8,}").search(user_password)
    password_upper = re.compile(r"[A-Z]").search(user_password)
    password_lower = re.compile(r"[a-z]").search(user_password)
    password_digits = re.compile(r"\d").search(user_password)
    if password_length and password_upper and password_lower and password_digits:
        return True
    else:
        return False


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
