# input
import keyword

data = keyword.kwlist


def min(strings: list[str], by_length=True) -> str:

    sort_param = lambda string: len(string) if by_length is True else string

    min_el = strings[0]

    for el in strings:
        if sort_param(min_el) > sort_param(el):
            min_el = el

    return min_el


print(min(data, by_length=True))
print(min(data, by_length=False))

# output
# as
# False
