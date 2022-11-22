# Start of the python demo

# Naming conventions

# Variable naming should be in lower case and be meaning full

# first_number = input("Enter the first number: ")
# second_number = input("Enter the second number: ")

# function names should be only in lower case $ if multiple name use underscore
# two line spaces should be provided between functions


# def my_function():
#     # four white spaces should be provided
#     first_number = int(input("Enter the first number: "))
#     second_number = int(input("Enter the second number: "))
#     total = first_number + second_number
#     return total


"""
 This block of comment is called multi line command
 Used for commands in which precedes more than one line
 into a block of comments
"""
import time

# print(my_function())

# def add(variable_one, variable_two,
#         # extra indentations should be provided to distinguish between arguments and the methods
#         variable_three, variable_four):
#     total = variable_one + variable_two + variable_three + variable_four
#     return total
#
#
# print(add(3, 5, 7, 9))


# def add(
#         variable_one, variable_two,
#         # extra indentations should be provided to distinguish between arguments and the methods
#         variable_three, variable_four):
#     total = variable_one + variable_two + variable_three + variable_four
#     return total
#
#
# print(add(3, 5, 7, 9))

# odd_number = 1
# even_number = 2
#
# if odd_number == 1 and even_number == 2:
#     print("Everything is equal")
#
# total_no_of_days = 20
# total_no_of_sundays = 5
# # operators should be placed before the operands
# total_working_days = (total_no_of_days
#                       - total_no_of_sundays)
#
# print(total_working_days)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
#
# x = "Python "
# y = "is "
# z = "awesome "
# print(x + y + z)
#
# languages = ["Tamil", "English", "Malayalam"]
# x, y, z = languages
#
# print(x, y, z)
#
# # declaring the scope as global
# first_name = "Dhanesh"
#
#
# def my_fun():
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# def my_fun():
#     global first_name  # changing the global variable
#     first_name = "Dinesh" # local variable with the scope within the function
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# def my_fun():
#     print("Welcome " + first_name)
#
#
# my_fun()
#
#
# language_list = ["Tamil", "English", "Malayalam"]  # list -> mutable
# language_tuple = ("Tamil", "English", "Malayalam")  # tuple -> immutable , small operation size
# x, y, z = 3, "Harini", 9
# print(id(x))
# # print(y)
# # print(id(y))
# y = "Siva"
# x = 27
# print(id(x))

# print(y)
# print(id(y))

# list_of_users = (["Dhanesh", "dk@123"], ["Harini", "hari@22"], ["Siva", "siva@mo"])
# print(list_of_users)
# list_of_users[2].append("siva@22")
# print(list_of_users)
# list_of_users.
# print(dir(list))
#
# list_of_languages = ['Java', 'Python']
# print(list_of_languages)
# list_of_tools = ['Flyway']
# print(list_of_tools)
# print(list_of_languages.__add__(list_of_tools))
#
# print(list_of_languages)

# import sys
#
#
# class ListExample:
#     grocery_list = ()
#     grocery_list2 = []
#     grocery_list3 = {}
#     grocery = ""
#
#     print(sys.getsizeof(grocery))
#     print(sys.getsizeof(grocery_list))
#     print(sys.getsizeof(grocery_list2))
#     print(sys.getsizeof(grocery_list3))

# print(dir(dict))
# # print(dir(list))
# x = 'Apple'
# X = 'pple'
#
# print(x == X)
# print(x.__contains__(X))
# print(x is X)
# first = {'id': {'name': 'Dhanesh', 'phone_number': '0987654321'}}
# second = {'name': 'Deepak', 'phone_number': '0987654321'}

# print(first.__sizeof__())
# # print(second.__sizeof__())
# # print(first.__eq__(second))
# # print(first.__class__)  # return the class of the data type
# # print(first.__contains__('name'))  # checks if the key is present or not
# # print(first.__class_getitem__(second))
# # print(first.__delitem__('phone_number'))
# print(first.popitem())
# print(first.__format__())
# print(second.__iter__())

# a = {}
# b = []
# c = ()
# # # print(a.__sizeof__())
# print(b.__sizeof__())
# print(c.__sizeof__())

# is operator & ==
