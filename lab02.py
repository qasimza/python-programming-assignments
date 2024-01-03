# CS2021 Lab 02
# Required Questions

#  RQ1
from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


#  RQ2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a+b*b+c*c - min(a*a, b*b, c*c)


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    "*** YOUR CODE HERE ***"
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i

         
#  RQ4
#  Write functions c, t, and f such that calling the with_if_statement and
#  calling the with_if_function do different things.
#  In particular, write functions (c,t,f) so that with_if_statement function returns the number 1, 
#  but calling the with_if_function function throws a ZeroDivisionError.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():  # returns 1
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()


def with_if_function(): # returns Zero division error
    return if_function(c(), t(), f())


def c():
    "*** YOUR CODE HERE ***"
    return True


def t():
    "*** YOUR CODE HERE ***"
    return 1


def f():
    "*** YOUR CODE HERE ***"
    return 1 % 0


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)