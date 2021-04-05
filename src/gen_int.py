from __future__ import annotations

import math
import random
from itertools import permutations

from src.exception import ArgRangeError


def generate_args(
    num: int, min: int, max: int, max_test_count: int
) -> list[tuple[int, ...]]:
    try:
        if math.factorial(num) > max_test_count:
            return generate_randints(num, min, max, max_test_count)
        else:
            return generate_permutations(num, min, max)
    except (OverflowError, MemoryError):
        raise ArgRangeError(min, max)


def generate_randints(
    num: int, min: int, max: int, max_test_count: int
) -> list[tuple[int, ...]]:
    args: set[tuple[int, ...]] = set()
    while len(args) < max_test_count:
        args.add(tuple(random.sample(range(min, max + 1), num)))
    return list(args)


def generate_permutations(num: int, min: int, max: int) -> list[tuple[int, ...]]:
    numbers = generate_randints(num, min, max, 1)[0]
    return [p for p in permutations(numbers)]
