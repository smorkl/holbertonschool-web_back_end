#!/usr/bin/env python3
wait_random = __import__("0-basic_async_syntax").wait_random
from typing import List
"""
simple asynchronous call
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays_list.append(float(delay))

    return sorted(delays_list)
