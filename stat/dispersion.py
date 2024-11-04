# input
data = [1, 2, 3, 4, 5]


def dispersion(array: list[int | float]) -> float:
    M = sum(array) / len(array)
    return sum([(el - M) ** 2 for el in array]) / (len(array) - 1)


print(dispersion(data))
# output
# 2.5
