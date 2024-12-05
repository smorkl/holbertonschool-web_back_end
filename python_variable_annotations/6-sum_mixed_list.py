#!/usr/bin/env python3
from typing import List, Union

"""
this fuction Calculates the sum of a list containing integers and floats.

fuction:
    sum_mixed_list(mxd_lst)
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst: A list of integers and floats.

    Returns:
        The sum of the elements in the list.
    """
    total = 0.0
    for num in mxd_lst:
        total += num
    return total
