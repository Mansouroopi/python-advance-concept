# A = [2, [3,4,’5’,6], [[[[[[23,940,’3333’]]]]]], [[9,],10]]
# Please flatten the list
# Ouput : [1,2, 3, 4, ‘5’, 6, 23,940,’3333’,9,10]
#https://stackabuse.com/python-how-to-flatten-list-of-lists/

# t = [2, [3,4,'5',6], [[[[[[23,940,'3333']]]]]], [[9,],10]]
# flat_list = [item for sublist in t for item in sublist]
# print(flat_list)

# method 1
l = [2, [3,4,'5',6], [[[[[[23,940,'3333']]]]]], [[9,],10]]
def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


print(flatten(l))


# method 2
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [2, [3,4,'5',6], [[[[[[23,940,'3333']]]]]], [[9,],10]]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))

# method 3
import functools
import operator
regular_list = []

# Transform irregular 2D list into a regular one.
def transform(nested_list):
    for ele in nested_list:
        if type(ele) is list:
            regular_list.append(ele)
        else:
            regular_list.append([ele])
    return regular_list


irregular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10], 11]
regular_2D_list = transform(irregular_list)
print('Original list', irregular_list)
print('Transformed list', functools.reduce(operator.iconcat, regular_2D_list, []))


#method 4
import itertools

regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
flat_list = list(itertools.chain(*regular_list))

print('Original list', regular_list)
print('Transformed list', flat_list)
