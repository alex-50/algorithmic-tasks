# input
data_odd_size = [i for i in range(1, 10)]  # 1...9
data_even_size = [i for i in range(1, 11)]  # 1...10


def median(array: list[int]) -> float:
    return (
        array[len(array) // 2]
        if len(array) % 2 != 0
        else sum(array[len(array) // 2 - 1 : len(array) // 2 + 1]) / 2
    )


print(median(data_odd_size))
print(median(data_even_size))

# output
# 5
# 5.5
