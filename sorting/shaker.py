from typing import Any

# input
data = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]


def shaker_sort(data: list[Any]) -> list[Any]:
    if data:
        left = 0
        right = len(data) - 1

        while left <= right:

            for i in range(right, left, -1):
                if data[i - 1] > data[i]:
                    data[i], data[i - 1] = data[i - 1], data[i]

            left += 1

            for i in range(left, right):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]

            right -= 1


shaker_sort(data)
print(data)

# output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
