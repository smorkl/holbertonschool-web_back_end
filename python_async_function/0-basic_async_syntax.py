#!/usr/bin/env python3
import random
import asyncio

max_delay: int = 10
async def wait_random() -> float :
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i