from multipledispatch import dispatch


@dispatch(int, float)
def sum1(a, b):
    print(a + b)


@dispatch(int, int)
def sum1(a, b):
    print(a + b)


try:
    sum1(3.5, 'a')
    a = 1 / 0


except ZeroDivisionError:
     print("divide by zero")


#it will catch the specific exception if it is defined or if Exception class is defined then it will go there
except Exception:  # Exception class is always triggered when it is first defined before other exception block
    print("Exception occurred.")

except NotImplementedError:
    print("the method is not implemented")


finally:
    print("I am in finally")