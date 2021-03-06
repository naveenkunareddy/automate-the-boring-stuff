#! /usr/bin/env python3
# comma_code.py - delimits collection of items using Oxford comma

from collections import Counter


def comma_code(collection):
    """
    Take an iterable collection and returns the collection as a string
    formatted using the Oxford comma

    :param collection: collection of values to convert to readable string
    """
    if len(collection) == 0:
        return ''
    elif len(collection) == 1:
        return str(collection[0])

    # list comprehension used to explicitly cast items to str str() converts
    # slice to list of chars, this implementation allows for a mixed list
    return f"{', '.join([str(item) for item in collection[:-1]])}, and {collection[-1]}"


if __name__ == '__main__':
    test = ['cat', 'dog', 'bird', 'snake', 'rock']
    test2 = [3, 4, 5, 6]
    print(comma_code(collection=test))
    print(comma_code(collection=test2))
    count = Counter(comma_code(collection=test))
    print(count[','])
    print(comma_code(collection=['apples', 'bananas', 'tofu', 'cats']))
