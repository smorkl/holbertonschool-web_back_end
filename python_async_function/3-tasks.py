#!/usr/bin/env python3
"""
the module Creates and returns
an asyncio.Task that will wait for a random
amount of time.
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that
    will wait for a random amount of time.

    Args:
      max_delay: The maximum number of seconds to wait.

    Returns:
      An asyncio.Task object representing the waiting task.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
