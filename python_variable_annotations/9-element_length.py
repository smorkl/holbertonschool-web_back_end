#!/usr/bin/env python3
from typing import List, Tuple

"""
This module provides a function to calculate the length of each element in a list.

The `element_length` function takes a list as input and returns a new list of tuples. Each tuple contains an element from the input list and its corresponding length.
"""

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculates the length of each element in a list of strings.

    Args:
        lst: A list of strings.

    Returns:
        A list of tuples, where each tuple contains a string from the input list and its length as an integer.
    """

    return [(i, len(i)) for i in lst]