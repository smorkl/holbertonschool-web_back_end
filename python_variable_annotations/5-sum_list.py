#!/usr/bin/env python3

"""
The module sums all the float data in a list.

fuction:
    sum_list(input_list): This function sums all the data in a list
"""


def sum_list(input_list: list[float]) -> float:
    """
    This function sums all the data in a list.

    arg:
        input_list: The list containing the numbers of floats.

    Return:
        result of adding the numbers in the list
    """
    for n in input_list:
        n += n
    return n
