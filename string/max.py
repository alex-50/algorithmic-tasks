# input
import keyword

data = keyword.kwlist


def max(strings: list[str], by_length=True) -> str:

    sort_param = lambda string: len(string) if by_length is True else string

    max_el = strings[0]

    for el in strings:
        if sort_param(max_el) < sort_param(el):
            max_el = el

    return max_el


print(max(data, by_length=True))
print(max(data, by_length=False))

# output
# continue
# yield
