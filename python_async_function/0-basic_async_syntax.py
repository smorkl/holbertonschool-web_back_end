#!/usr/bin/env python3
import random
import asyncio
from typing import Union

max_delay: int = 10
async def wait_random() -> Union[float, int] :
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i