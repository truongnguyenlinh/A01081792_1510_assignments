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
    [2, 10, 23]
    >>> time_calculator(1)
    [1]
    """
    days = 86400
    hours = 3600
    minutes = 60
    sec = 1

    if not seconds > 0:
        raise ValueError("Number given is not a positive.")

    time_convert = []

    if seconds >= days:
        seconds_to_days = seconds // days
        time_convert.append(seconds_to_days)
        seconds = seconds % days

    if seconds >= hours:
        seconds_to_hours = seconds // hours
        time_convert.append(seconds_to_hours)
        seconds = seconds % hours

    if seconds >= minutes:
        seconds_to_min = seconds // minutes
        time_convert.append(seconds_to_min)
        seconds = seconds % minutes

    if seconds >= sec:
        sec_only = seconds // sec
        time_convert.append(sec_only)

    return time_convert


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

