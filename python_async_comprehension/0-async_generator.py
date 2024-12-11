#!/usr/bin/env python3
"""
The module runs 10
times and randomly gives a number from 1 to 10
"""
import asyncio
import random

async def async_generator():
    """
    Asynchronously generates 10 random
    numbers between 0 and 10, with a 1-second
      delay between each number.

    Yields:
        int: A random integer between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
