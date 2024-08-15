from math import log2
from itertools import product

# input
conjunction = [0, 0, 0, 1]
disjunction = [0, 1, 1, 1]
my_function = [0, 0, 1, 1]


def is_free_variable(func_vector: list[bool], pos: int) -> bool:

    size = log2(len(func_vector))
    pos -= 1

    if not size.is_integer():
        return "Bad args: len(func_vector) != 2, 4, 8, 16 ..."
    elif pos >= size:
        return "Out of range of args"

    tmp_args = list(map("".join, product(["0", "1"], repeat=int(size) - 1)))

    for tmp_arg in tmp_args:
        first_args = tmp_arg[:pos] + "0" + tmp_arg[pos:]  # 01010_0_0101 ...
        second_args = tmp_arg[:pos] + "1" + tmp_arg[pos:]  # 01010_1_0101 ...

        n1, n2 = map(lambda x: int(x, 2), [first_args, second_args])

        if func_vector[n1] != func_vector[n2]:
            return False

    return True


print(is_free_variable(conjunction, 2))
print(is_free_variable(disjunction, 2))
print(is_free_variable(my_function, 2))

# output
# False
# False
# True
