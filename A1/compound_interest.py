# Linh Truong
# A01081792
# 01-25-2019


import doctest


def compound_interest(principle, annual_interest_r, n_years_comp, years):
    """Print the compound interest of initial deposit given interest rate and total years.

    PARAM: principle: a float
    PARAM: annual_interest: a float
    PARAM years_comp: an int
    PARAM years: an int
    PRECONDITION: principle must be a float
    PRECONDITION: annual_interest must be a float
    PRECONDITION: years_comp must be an integer
    PRECONDITION: years must be an integer
    >>> compound_interest(6078.0, 0.10, 7, 8)
    13450.4862
    >>> compound_interest(0.0, 1.0, 1, 0)
    0.0
    """
    total_money = float(principle) * ((1 + float(annual_interest_r) / int(n_years_comp)) ** (int(n_years_comp*years)))
    return total_money


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

