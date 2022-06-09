#!/usr/bin/env python3
""" Async comprehensing"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    use an async comprehension over async_generator, 
    returning 10 random numbers
    """
    return [i async for i in async_generator()]
