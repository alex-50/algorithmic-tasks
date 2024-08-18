# input
# n = 1, 10, 30


def get_fibbonachi_row_to_n(n: int) -> list[int]:
    fib_numbers = [1, 1]

    for i in range(n - 2):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers[:n]


print(get_fibbonachi_row_to_n(1))
print(get_fibbonachi_row_to_n(10))
print(get_fibbonachi_row_to_n(30))

# output
# [1]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
