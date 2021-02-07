
# A = [“Ali”,”Hamza”,”Usman”]

# B = [ [ 23, 29, 32], [ 5.8, 5.9, 6.1] ...]
#
# Ali is 23 years old and his height is 5.8ft
# print(f"{} is {} years old  and hhis height is {}ft.".format(a, b[0], b[1]))
# Hamza is 29 years old and his height is 5.9ft.
# def person(A, B):
#     for a, b in zip(A, B):
#         print(a, " is ", b[0], " years old and his height is", b[1], 'ft')
#
# A = ["Ali","Hamza","Usman"]
# B = [[ 23, 29, 32], [ 5.8, 5.9, 6.1]]
#
# person(A, B)

# Q 2
# List a contains 100 words, many of them are duplicate, write a two line code which removes duplicates preserving the order of list.

# my_list = ['mansour', 'mansour', 'hassani', 'abdalla']
# my_set = list(set(my_list))

# Q#

# Q3- Assuming that we have some email addresses in the "username@companyname.com" format, please write program that;
# Print the “user name” of a given email address.
# Prints the “companyname” of a given email address

# def username_from_email(email):
#     u = []
#     for item in email:
#         if item == '@':
#             break
#         u.append(item)
#     return ''.join(u)
#
# print(username_from_email('socker@companyname.com'))


# Q4
# Q4 - Given two given lists [1,3,6,78,35,55] and [12,24,35,55,88,78,155],
# write a program to make a list whose elements are intersection of the above given lists.
# def get_intersection_of_two_list(a, b):
#     a_intesect_b = list(set(a).intersection(set(b)))
#     print(a_intesect_b)
#
# a = [1,3,6,78,35,55]
# b = [12,24,35,55,88,78,155]
# get_intersection_of_two_list(a, b)


# Q5
# Q5- Write a recursive function which calculates 1+2+3+...+10
# e.g. sum_recursive (start = 1 , end = 10)
#
#        output = 55

def sum_recursive(start = 1 , end = 10):
    sum = 0; # iterative
    for i in range(end+1):
        sum+=i
    print(sum)
    #end iterative

    # recursive
    # while end > start:
    #     return int(start) + int(sum_recursive(start, end-1))


print(sum_recursive(1,10))


# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 10

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
