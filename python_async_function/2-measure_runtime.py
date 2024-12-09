#!/usr/bin/env python3
"""
This module imports the wait_n function
and executes it n times, and at the end
we return the average of the time it took to execute.
"""

wait_n = __import__("1-concurrent_coroutines").wait_n
import time
import asyncio


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay) and returns the average time per call.

    Args:
        n: Number of coroutines to wait for.
        max_delay: Maximum delay for each coroutine in seconds.

    Returns:
        Average execution time per coroutin call (float).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
