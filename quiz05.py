"""

>>> test_list = [1,2,3]
>>> is_sorted(test_list)
True

>>> test_list = [3,2,4,0]
>>> is_sorted(test_list)
False
"""


def is_sorted(test_list):
    sorted_list = sorted(test_list)
    return sorted_list == test_list
