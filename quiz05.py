"""
    Is list sorted

    Checks to see if a list is sorted in ascending order
    :param test_list: a list of n integers; n >= 0
    :precondition: must give a list, must only contain integers
    :postcondition: checks to see if list is sorted
    :return: True or False is list is sorted

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
