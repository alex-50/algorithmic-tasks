from typing import Any

# input
data = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]


def bubble_sort(data: list[Any]) -> list[Any]:
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]


bubble_sort(data)
print(data)

# output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
