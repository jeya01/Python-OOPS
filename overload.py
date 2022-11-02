from multipledispatch import dispatch


# @dispatch(int, int, int)
# def sum1(a, b, c):
#     print(a + b + c)
#
#
# @dispatch(int, int)
# def sum1(a, b):
#     print(a + b)
#
#
# sum1(1, 2, 3)

@dispatch(int, float)
def sum1(a, b):
    print(a + b)


@dispatch(int, int)
def sum1(a, b):
    print(a + b)


sum1(3, 3.5)
