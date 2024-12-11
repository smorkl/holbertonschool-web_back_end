#!/usr/bin/env python3
"""
This script demonstrates the use of asynchronous comprehensions in Python.

It imports an asynchronous generator function
`async_generator` from the `0-async_generator` module.
This function generates random numbers asynchronously,
with a one-second delay between each number.

The `async_comprehension` function uses
an asynchronous comprehension to efficiently
collect these random numbers.
The comprehension iterates over the numbers
yielded by `async_generator`,
and for each number, it adds it to a list.

The final list of 10 random numbers is returned by
the `async_comprehension` function.
"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Asynchronously collects 10 random numbers generated by `async_generator`.

    Returns:
        list: A list of 10 random integers.
    """

    num_ten = [i async for i in async_generator()]
    return num_ten
