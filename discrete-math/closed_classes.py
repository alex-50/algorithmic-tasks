from math import log2


class ClosedClasses:
    def __init__(self, func_vector: list[bool]) -> None:

        if not log2(len(func_vector)).is_integer():
            raise "Bad argument"

        self.func_vector = func_vector

    def is_T0(self) -> bool:
        return self.func_vector[0] == 0

    def is_T1(self) -> bool:
        return self.func_vector[-1] == 1

    def is_S(self) -> bool:
        return (
            self.func_vector[: len(self.func_vector) // 2]
            == self.func_vector[len(self.func_vector) // 2 :][::-1]
        )

    def is_L(self) -> bool:
        # Pascal's triangle method
        tmp = self.func_vector
        iteration_count = 0

        while tmp:
            if tmp[0] == 1 and bin(iteration_count).count("1") > 1:
                return False

            tmp = [tmp[i] ^ tmp[i + 1] for i in range(len(tmp) - 1)]
            iteration_count += 1

        return True

    def is_M(self) -> bool:
        all_args = [
            (len(bin(len(self.func_vector) - 1)) - len(bin(i))) * "0" + bin(i)[2:]
            for i in range(len(self.func_vector))
        ]
        comparable_args = {arg: [] for arg in all_args}

        for alpha in all_args:
            for beta in all_args:

                for i in range(int(log2(len(self.func_vector)))):
                    if alpha[i] > beta[i]:
                        break
                else:
                    if alpha != beta:
                        comparable_args[alpha].append(beta)

        for alpha in comparable_args:
            for beta in comparable_args[alpha]:
                if self.func_vector[int(alpha, 2)] > self.func_vector[int(beta, 2)]:
                    return False

        return True

    def criteria_of_completeness_of_the_Post(self) -> bool:
        return not any(
            [self.is_T0(), self.is_T1(), self.is_S(), self.is_L(), self.is_M()]
        )


# input

functions = {
    "Pierces arrow": [1, 0, 0, 0],
    "conjunction": [0, 0, 0, 1],
    "Schaeffers stroke": [1, 1, 1, 0],
    "disjunction": [0, 1, 1, 1],
}


for func in functions:
    print(
        f'"{func}" - the criteria of the Post: {ClosedClasses(functions[func]).criteria_of_completeness_of_the_Post()}'
    )

# output
# "Pierces arrow" - the criteria of the Post: True
# "conjunction" - the criteria of the Post: False
# "Schaeffers stroke" - the criteria of the Post: True
# "disjunction" - the criteria of the Post: False
