from math import log2


def generate_CCNF_expression(func_vector: list[bool]) -> str:

    if not log2(len(func_vector)).is_integer():
        raise ValueError("Bad argument")

    if not any(func_vector):
        return "0"

    multipliers = []

    for i in range(len(func_vector)):
        if not func_vector[i]:
            args = (len(bin(len(func_vector) - 1)) - len(bin(i))) * "0" + bin(i)[2:]
            multiplier = "("
            for num, arg in enumerate(args):

                multiplier += f"not(X{num + 1})" if arg == "0" else f"X{num + 1}"
                multiplier += " or " if num != len(args) - 1 else ")"

            multipliers.append(multiplier)
    return " and ".join(multipliers) if multipliers else None


# input
conjunction = [0, 0, 0, 1]
disjunction = [0, 1, 1, 1]
const_0 = [0, 0]
const_1 = [1, 1, 1, 1, 1, 1, 1, 1]


print(generate_CCNF_expression(conjunction))
print(generate_CCNF_expression(disjunction))
print(generate_CCNF_expression(const_0))
print(generate_CCNF_expression(const_1))

# output
# (not(X1) or not(X2)) and (not(X1) or X2) and (X1 or not(X2))
# (not(X1) or not(X2))
# 0
# None
