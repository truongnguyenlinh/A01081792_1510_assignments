# Linh Truong
# A01081792
# 01-25-2019


import doctest


def time_calculator(seconds):
    """Converts given seconds to days, hours, minutes and seconds.

    PARAM seconds: integer
    PRECONDITION seconds: value given must be a positive integer
    POST-CONDITION seconds: generate equivalent conversion from given seconds
    RETURN list of integers converting to days, hours, minutes or seconds
    >>> time_calculator(99999)
    [1, 3, 46, 39]
    >>> time_calculator(7823)
    [0, 2, 10, 23]
    >>> time_calculator(1)
    [0, 0, 0, 1]
    """
    days = 0
    hours = 0
    minutes = 0

    if not seconds > 0:
        return "Number given is not a positive."

    if seconds >= 86400:
        days = seconds // 86400
        seconds = seconds % 86400

    if seconds >= 3600:
        hours = seconds // 3600
        seconds = seconds % 3600

    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60

    time_convert = [days, hours, minutes, seconds]

    return time_convert


def main():
    """Execute the program."""
    doctest.testmod()


if __name__ == '__main__':
    main()

