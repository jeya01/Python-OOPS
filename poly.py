class Sum:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def do_sum(self,a,b):
        print(f'sum:',self.a+self.b) # ex using instance variable
        # print(f'sum' , a + b) # ex using local variable

s = Sum(1,2)
s.do_sum(3,4)


'''Method overloading is not supported by python'''


# def do_sum(a, b):
#     print(a + b)
#
#
# def do_sum_three_param(a, b, c):
#     print(a + b + c)
