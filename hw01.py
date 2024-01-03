_author_ = "Zaina Qasim"
_credits_ = ["https://airbrake.io/blog/python-exception-handling/overflowerror to look up what is overflow error"
             "https://stackoverflow.com/questions/10121861/dividing-large-numbers-in-python to look up ways to divide very large nmubers"]
_email_ = "qasimza@mail.uc.edu"


def egypt(n, d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    >>> egypt(2,3)
    '1/2 + 1/6 = 2/3'
    """
    f_list = []
    n0, d0 = n, d
    while n0 != 0:
        di = d0 // n0 if d0 % n0 == 0 else d0 // n0 + 1  # next smallest denominator
        n0 = n0*di - d0  # calculating numerator after subtraction
        d0 = d0 * di  # calculating denominator after subtraction
        f_list.append(f'1/{di}')  # storing egypt fraction in list
    print(f'\'{" + ".join(f_list)} = {n}/{d}\'')  # displaying the egypt sequence in correct format


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
