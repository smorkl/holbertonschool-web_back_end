#!/usr/bin/env python3\
"""
This module provides a function to create a tuple from a key-value pair.

The key must be a string, and the value can be either an integer or a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a key-value pair.

    Args:
        k: The key, a string.
        v: The value, an integer or a float.

    Returns:
        A tuple containing the key and value.
    """

    tuple = (k, v**2)
    return tuple
