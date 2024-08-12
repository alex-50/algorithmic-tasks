from typing import Any

# input
data = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]


def max(numbers: list[Any]) -> Any:

    max_el = numbers[0]

    for el in numbers:
        if max_el < el:
            max_el = el

    return max_el


print(max(data))

# output
# 9
