#See the analog in the "math" folder
# input
a = 12
b = 18


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(a, b))
# output
# 6
