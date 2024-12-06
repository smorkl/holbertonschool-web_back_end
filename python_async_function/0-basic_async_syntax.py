#!/usr/bin/env python3
"""
simple asynchronous call
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait.
            Defaults to 10.

    Returns:
        float: The actual number of seconds waited.
    """
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i
