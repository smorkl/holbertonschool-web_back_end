#!/usr/bin/env python3
"""
simple asynchronous call
"""
from '0-basic_async_syntax.py' import wait_random
from typing import List

async def wait_n (n: int, max_delay: int) -> List[float]:
    i = 0
    list = ()
    while i <= n:
        list.append(wait_random(max_delay))
        i += 1
    list = sorted(list)
    return list