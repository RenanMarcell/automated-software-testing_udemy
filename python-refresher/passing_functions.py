def methodception(another):
    return another(30, 13)


def add_two_numbers(*args):
    return sum(args)


print(methodception(add_two_numbers))


print(methodception(lambda x, y: x + y))
