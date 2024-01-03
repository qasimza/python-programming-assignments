##Lab04 Required Questions ##

_author_ = "Zaina Qasim"
_credits_ = ["Michael Reynolds, reynomo@mail.uc.edu"]
_email_ = "qasimza@mail.uc.edu" # Your email address

#NOTE: Discussed problems with Michael

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    return lst+lst[::-1]


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"
    return [fn(fn(i)) for i in seq]


# RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    return [i for i in seq if not pred(i)]


# RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    return [i for i in range(n) if pred(i)]

# RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]]
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"
    l = []
    for i in lst:
        if isinstance(i, list):
            l = l + flatten(i)
        else:
            l.append(i)
    return l

