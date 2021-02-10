def smart(func):
    """ Decorator function """
    def inner(*args, **kwargs):
        """ Wrapper function"""
        if kwargs['b'] == 0:
            print("OOOPS! can not devide by zero")
            return
        return func(*args, **kwargs)
    return inner


@smart
def devide(a, b):
    return a / b

result  = devide(a=10, b=5)
print(result)
my_tupple = iter((i for i in range(10)))
for i in my_tupple:
    print(i, end=", ")
