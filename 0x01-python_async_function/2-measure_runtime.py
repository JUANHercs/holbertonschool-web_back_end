#!/usr/bin/env python3
""" Function measure time, async module"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n"""
    t1 = time()
    asyncio.run(wait_n(n, max_delay))
    t2 = time()
    return (t2 - t1) / n
