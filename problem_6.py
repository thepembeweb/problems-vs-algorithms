import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return "Invalid input! Please input a list containing one or more integers."
    min_integer = 0
    max_integer = 0
    for integer in ints:
        if integer >= 0:
            min_integer = min(min_integer, integer)
            max_integer = max(max_integer, integer)
        else:
            return "Invalid input"
    return (min_integer, max_integer)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
# should return a tuple (0, 9)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

ints = [0, -1]
print(ints)
# should return a warning message
print("Pass" if ("Invalid input" == get_min_max(ints)) else "Fail")

ints = [0]
print(ints)
# should return (0, 0)
print("Pass" if ((0, 0) == get_min_max(ints)) else "Fail")

ints = []
print(ints)
# should return a warning message.
print(get_min_max(ints))
