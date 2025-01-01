from typing import Union


def add(a: Union[int, float], b: int) -> int | float:
    return a + b


print(add(1, 2))
