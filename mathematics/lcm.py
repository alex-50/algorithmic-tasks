from math import gcd

#input
a = 12
b = 18


def lcm(a, b):
    return a * b // gcd(a, b)


print(lcm(a, b))

#output
#36
