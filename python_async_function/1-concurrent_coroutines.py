#!/usr/bin/env python3
"""
simple asynchronous call
"""
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List

async def wait_n (n: int, max_delay: int) -> List[float]:
    i = 0
    list = ()
    while i <= n:
        list.append(wait_random(max_delay))
        i += 1
    list = sorted(list)
    return list