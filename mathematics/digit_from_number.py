from math import log10
from datetime import datetime

# input
x = int(datetime.now().timestamp())


def get_digit_from_number(n: int, pos: int) -> int:
    return (n % 10**pos) // 10 ** (pos - 1)


print(x)
print({i: get_digit_from_number(x, i) for i in range(1, len(str(x)) + 1)})

# output
# 1724148795
# {1: 5, 2: 9, 3: 7, 4: 8, 5: 4, 6: 1, 7: 4, 8: 2, 9: 7, 10: 1}
