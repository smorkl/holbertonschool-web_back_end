#!/usr/bin/env python3
"""
This module executes the async comprehension
function 4 times and returns the execution time
"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the execution time of running the
    `async_comprehension` function four times
    concurrently.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]

    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
