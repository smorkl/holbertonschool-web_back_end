#!/usr/bin/env python3
from typing import List
"""
this fuction Calculates the sum of a list containing integers and floats.
"""
def sum_mixed_list (mxd_lst: List[float, int]) -> float:
    """Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst: A list of integers and floats.

    Returns:
        The sum of the elements in the list.
    """
    total = 0.0
    for num in mxd_lst:
        total += num
    return total

