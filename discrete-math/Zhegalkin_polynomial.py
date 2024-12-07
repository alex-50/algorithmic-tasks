from math import log2


def generate_Zhegalkin_polynomial_expression(func_vector: list[bool]) -> str:

    if not log2(len(func_vector)).is_integer():
        raise ValueError("Bad argument")

    if all(func_vector):
        return "1"

    tmp_row = func_vector
    polynomials = []
    iteration_count = 0

    while tmp_row:

        if tmp_row[0] == 1:
            args = (
                len(bin(len(func_vector) - 1)) - len(bin(iteration_count))
            ) * "0" + bin(iteration_count)[2:]
            polynomial = ""

            for num, arg in enumerate(args):
                if arg == "1":

                    polynomial += f"X{num + 1}"

                    if args[num + 1 :].count("1"):
                        polynomial += " and "
                    else:
                        if "and" in polynomial:
                            polynomial = f"({polynomial})"
                        break

            if polynomial:
                polynomials.append(polynomial)

        tmp_row = [tmp_row[i] ^ tmp_row[i + 1] for i in range(len(tmp_row) - 1)]
        iteration_count += 1

    return " ^ ".join(polynomials) if polynomials else None


# input
conjunction = [0, 0, 0, 1]
disjunction = [0, 1, 1, 1]
const_0 = [0, 0]
const_1 = [1, 1, 1, 1, 1, 1, 1, 1]


print(generate_Zhegalkin_polynomial_expression(conjunction))
print(generate_Zhegalkin_polynomial_expression(disjunction))
print(generate_Zhegalkin_polynomial_expression(const_0))
print(generate_Zhegalkin_polynomial_expression(const_1))

# output
# (X1 and X2)
# X2 ^ X1 ^ (X1 and X2)
# None
# 1
