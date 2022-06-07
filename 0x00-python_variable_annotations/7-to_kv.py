#!/usr/bin/env python3
""" Type-annotated function to_kv """
import math
from typing import List, Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple witha string and float"""
    num: float = float(v ** 2)
    return (k, num)
