#!/usr/bin/env python3
"""write an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that takes an integer argument and waits
    for an random delay and eventually returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
