#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function to create a multiplier function.

The `make_multiplier` function is useful when you need a function
that applies a consistent multiplication factor to any given float input.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The value by which inputs to the returned function will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the product of the input and the multiplier.

    Example:
        >>> multiplier_function = make_multiplier(3.0)
        >>> multiplier_function(2.0)
        6.0

    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the given value by the multiplier.

        Args:
            value (float): The number to be multiplied by the multiplier.

        Returns:
            float: The product of `value` and `multiplier`.

        Example:
            >>> multiplier_function(2.5)
            7.5  # Assuming the multiplier is 3.0
        """
        return value * multiplier

    return multiplier_function
