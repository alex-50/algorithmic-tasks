data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mean(array: list[int | float]) -> float:
    return sum(array) / len(array)

print(mean(data))
# output 
# 5.0