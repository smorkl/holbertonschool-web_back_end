#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function to create a multiplier function.

The `make_multiplier` function takes a float as input and returns a new function that multiplies its input by the given multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""

    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
