from math import log10

# input
numbers = [n**n for n in range(1, 10)]


def get_number_lenght(n: int) -> int:
    return int(log10(n)) + 1


for n in numbers:
    print(f'Size of "{n}": {get_number_lenght(n)}')

# output
# Size of "1": 1
# Size of "4": 1
# Size of "27": 2
# Size of "256": 3
# Size of "3125": 4
# Size of "46656": 5
# Size of "823543": 6
# Size of "16777216": 8
# Size of "387420489": 9
