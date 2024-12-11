#!/usr/bin/env python3
"""
simple asynchronous call
"""
#!/usr/bin/env python3
"""
simple asynchronous call
"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a specified number of random delays.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay in seconds for each wait.

    Returns:
        List[float]: A list of the actual delays in seconds.
    """
    delays_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays_list.append(float(delay))

    return sorted(delays_list)
