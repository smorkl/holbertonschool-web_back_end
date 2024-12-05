#!/usr/bin/env python3
from typing import Callable
"""
This module provides a function to create a multiplier function.

The `make_multiplier` function takes a float as input and returns a new function that multiplies its input by the given multiplier.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier: The factor to multiply by.

    Returns:
        A function that multiplies its input by the given multiplier.
    """
    return (multiplier * multiplier)