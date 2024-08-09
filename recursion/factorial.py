#See the analog in the "math" folder
# input
data = [i for i in range(10)]


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


print(*map(factorial, data))

# output
# 0 1 2 6 24 120 720 5040 40320 362880
