'''this is used to add as many items to be added  also the same used for multiplication'''
'''check List vs tuple'''
def addition(args):
    def add(*agrs):
        sum = 0
        for a in args:
            sum = sum + a
        print(f'sum is{sum}')
    add(*args)

number_tuple=(11,2,3,4,5,5)
addition(number_tuple)

def multiplication(args):
    def multiple(*args):
        m = 1
        for i in args:
            m = m * i
        print(f"multiple is : {m}")
    multiple(*args)


number_list = [1,2,3,4,5]
multiplication(number_list)

