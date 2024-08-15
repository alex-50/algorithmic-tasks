from typing import Callable
from inspect import signature

#input
conjunction = lambda a, b: a and b
disjunction = lambda a, b: a or b
const_1 = lambda a: a or not a
const_0 = lambda b: b and not b


def generate_bool_func_vector(bool_func: Callable[..., bool]) -> list[bool]:

    output = []
    arg_count = len(signature(bool_func).parameters)

    for i in range(2**arg_count):
        current_args_str = (len(bin(2**arg_count - 1)) - len(bin(i))) * "0" + bin(i)[2:]
        current_args = list(
            map(lambda arg: True if arg == "1" else False, current_args_str)
        )
        output.append(bool_func(*current_args))

    return output


print(generate_bool_func_vector(conjunction))
print(generate_bool_func_vector(disjunction))
print(generate_bool_func_vector(const_0))
print(generate_bool_func_vector(const_1))

#ouput
# [False, False, False, True]
# [False, True, True, True]
# [False, False]
# [True, True]


