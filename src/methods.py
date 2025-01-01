"""
this function will
example:
add_numbers(4) = 1+2 + 3+4
"""

from functools import reduce


def add_numbers(number: int) -> int:
    result = 0
    for i in range(1, number + 1):
        result += i

    return result


result = add_numbers(6)

print(result)


def add_numbers_2(number: int) -> int:
    return sum(range(1, number + 1))


print(add_numbers_2(6))


def add_numbers_recursion(number: int) -> int:
    if number == 0:
        return 0
    return number + add_numbers_recursion(number - 1)


print(add_numbers_recursion(6))

list_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add_two(acc, i): return acc + i


results = reduce(add_two, list_ten)
print(result)
