#!/usr/bin/env python3
from typing import Callable, float

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

    def multiply(x: float) -> float:
        """
        Multiplies the input by the multiplier.

        Args:
            x: The number to multiply.

        Returns:
            The product of x and the multiplier.
        """
        return x * multiplier

    return multiply
