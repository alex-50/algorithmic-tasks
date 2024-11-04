from random import randint

# input
data = [randint(1, 5) for _ in range(100)]
"""
[3, 1, 3, 3, 4, 4, 4, 2, 5, 4, 1, 1, 2, 1, 5, 1, 1, 1, 1, 5, 5, 2, 4, 3, 2, 3, 1, 4, 2, 4, 1, 5, 3, 2, 4, 3, 2, 4, 4, 4, 4, 2, 5, 5, 3, 4, 2, 3, 4, 3,
 3, 5, 2, 4, 2, 3, 5, 2, 2, 1, 2, 1, 5, 5, 1, 3, 2, 1, 4, 3, 5, 3, 1, 1, 3, 5, 2, 2, 3, 2, 1, 4, 2, 3, 4, 1, 4, 5, 2, 4, 3, 4, 3, 3, 4, 1, 1, 2, 5, 2]
"""


def mode(array: list[int | float]) -> list[int | float]:
    counter = dict(
        sorted(
            {value: array.count(value) for value in set(array)}.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )
    max_repeat = max(counter.values())
    return list(
        map(
            lambda item: item[0],
            filter(lambda item: item[1] == max_repeat, counter.items()),
        )
    )


print(mode(data))
# output
# [2, 4]
