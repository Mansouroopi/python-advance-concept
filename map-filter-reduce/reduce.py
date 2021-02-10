# reduce(function, sequence[, initial])

from functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))



# lambda
list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))


my_list = [i for i in range(11)]
new_list = reduce(lambda x, y: x+y, my_list)
print(new_list)
