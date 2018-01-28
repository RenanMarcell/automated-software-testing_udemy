def my_method(arg1, arg2):
    return arg1 + arg2


print(my_method(5, 6))


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def my_list_addition(list_arg):
    return sum(list_arg)


print(my_long_method(1, 2, 3, 4, 5, 6))
print(my_list_addition([1, 3, 5, 7, 9]))


def addition_simplified(*args):
    return sum(args)


print(addition_simplified(1, 2, 3, 4, 5))

##




