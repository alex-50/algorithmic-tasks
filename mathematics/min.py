from typing import Any

# input
data = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]


def min(numbers: list[Any]) -> Any:

    min_el = numbers[0]

    for el in numbers:
        if min_el > el:
            min_el = el

    return min_el


print(min(data))

# output
# 0
