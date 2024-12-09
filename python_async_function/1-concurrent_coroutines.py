#!/usr/bin/env python3
"""
simple asynchronous call
"""
wait_random = __import__("0-basic_async_syntax").wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays_list.append(float(delay))

    return sorted(delays_list)
