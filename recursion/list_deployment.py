# input
data = [1, [2, 3], [[4], [5], 6], [[[7, 8], 9]], 10]


def deploy(list_object: list) -> list:
    root = []
    for el in list_object:
        if type(el) is list:
            root.extend(deploy(el))
        else:
            root.append(el)
    return root


data = deploy(data)
print(data)

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
