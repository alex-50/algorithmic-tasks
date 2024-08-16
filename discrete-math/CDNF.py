from math import log2


def generate_CDNF_expression(func_vector: list[bool]) -> str:

    if not log2(len(func_vector)).is_integer():
        raise "Bad argument"

    if all(func_vector):
        return "1"

    terms = []

    for i in range(len(func_vector)):
        if func_vector[i]:
            args = (len(bin(len(func_vector) - 1)) - len(bin(i))) * "0" + bin(i)[2:]
            term = "("
            for num, arg in enumerate(args):

                term += f"not(X{num + 1})" if arg == "0" else f"X{num + 1}"
                term += " and " if num != len(args) - 1 else ")"

            terms.append(term)
    return " or ".join(terms) if terms else None


# input
conjunction = [0, 0, 0, 1]
disjunction = [0, 1, 1, 1]
const_0 = [0, 0]
const_1 = [1, 1, 1, 1, 1, 1, 1, 1]


print(generate_CDNF_expression(conjunction))
print(generate_CDNF_expression(disjunction))
print(generate_CDNF_expression(const_0))
print(generate_CDNF_expression(const_1))

# output
# (X1 and X2)
# (not(X1) and X2) or (X1 and not(X2)) or (X1 and X2)
# None
# 1
