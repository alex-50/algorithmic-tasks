#See the analog in the "recursion" folder
#  input
a = 12
b = 18


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


print(gcd(a, b))
# output
# 6
