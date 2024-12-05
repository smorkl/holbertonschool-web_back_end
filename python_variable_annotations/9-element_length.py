#!/usr/bin/env python3
"""
This module provides a function to calculate
 the length of each element in a list.

The `element_length` function accepts an iterable
of sequences and returns a list of tuples. Each tuple
contains an element from the input iterable and its corresponding length.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list of strings.

    Args:
        lst: A list of strings.

    Returns:
        A list of tuples, where each tuple contains
        a string from the input list and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
