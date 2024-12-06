#!/usr/bin/env python3
import random
import asyncio

max_delay = 10
async def wait_random():
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i