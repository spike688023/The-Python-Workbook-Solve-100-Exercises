#Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)

#Video question so that user sees the pretty print


"""

哎, 這次的建法, 就相同了.

但它多用了個  pprint ,  我想是增加可讀性而己吧

NAME
    pprint - Support to pretty-print lists, tuples, & dictionaries recursively.

    pprint()
        Pretty-print a Python object to a stream [default is sys.stdout].


>>> e = dict( a = list(range(1,11)) , b=list(range(11,21)), c=list(range(21,31)) )
>>> e
{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}

"""
