# See the analog in the "recursion" folder
# input
data = [i for i in range(10)]


def factorial(n: int) -> int:

    result = 1

    for i in range(n):
        result *= n - i

    return result


print(*map(factorial, data))

# output
# 1 1 2 6 24 120 720 5040 40320 362880
