## Lab 5: Required Questions - Dictionaries Questions ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    new_dict = dict1
    for e in dict2:
        new_dict[e] = dict2[e]
    return new_dict


# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"
    words = message.split()
    freq_table = {}
    for e in words:
        if e in freq_table:
            freq_table[e]+=1
        else:
            freq_table[e] = 1
    return freq_table


# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for e in d:
        if d[e] == x:
            d[e] = y

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   "*** YOUR CODE HERE ***"
   sum_dict = {}
   for dictionary in lst:
       for e in dictionary:
           if e in sum_dict:
               sum_dict[e] += dictionary[e]
           else:
               sum_dict[e] = dictionary[e]

   return sum_dict

#RQ5

def build_successors_table(tokens):
    """Takes in a list of words or tokens. Return a dictionary: keys are words; values are lists of successor words.
    By default, we set the first word in tokens to be a successor to "."

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table


def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += f'{word} '
        word = random.choice(table[word])
    return result + word

def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)


def middle_tweet(word, table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string that is of length right in middle of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    "*** YOUR CODE HERE ***"
    tweets = [random_tweet(table) for i in range(5)]
    tweets = sorted(tweets, key=len)
    return tweets[2]

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

shakestokens = shakespeare_tokens()
shakestable = build_successors_table(shakestokens)


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
