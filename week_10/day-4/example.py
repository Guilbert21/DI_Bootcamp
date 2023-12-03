# data_list = [1,2,3,4]
# print(data_list)

# # swap position [1] to position [2]
# data_list[1], data_list[2] = data_list[2], data_list[1]

# print(data_list)

from time import time

# def timer(func):

#     def wrapper(*args, **kwargs):
#         start = time()
#         func(*args, **kwargs)
#         end = time()
#         print(f"Time <{func.__name__}>: {end-start}")

#     return wrapper

# @timer
# def function_to_measure(arg1, arg2):
#     for i in range(1000000):
#         useless_var = i * i**i

# function_to_measure(1, 1000000)

# # The decorator
# def is_called(func_as_arg):
#     # The wrapper function
#     def is_returned():
#         print("Hello")
#         func_as_arg()
#     # returns the wrapper address
#     return is_returned

# def func_as_arg():
#      print("Bye")

# new = is_called(func_as_arg)
# new()


# # Example without decorator
# def my_decorator(called_function):
#     def new_function():
#         print("Hello world from the decorator")
#         called_function()
#     return new_function

# def print_helloworld():
#     print("Hello world from the function")

# # What happens in the line below ?
# print(my_decorator(print_helloworld))
# # >> <function my_decorator.<locals>.new_function at 0x7f5e4e58d790>
# # The output is the function returned by the function my_decorator()

# # So, we have to call this function to print the two sentences
# print(my_decorator(print_helloworld)())
# # >> Hello world from the decorator
# # >> Hello world from the function




# # Example with the decorator
# def my_decorator(called_function):
#     def new_function():
#         print("Hello world from the decorator")
#         called_function()
#     return new_function

# @my_decorator
# def print_helloworld():
#     print("Hello world from the function")

# print_helloworld()
# # >> Hello world from the decorator
# # >> Hello world from the function

# # The same as writing 
# print_helloworld = my_decorator(print_helloworld)
# print_helloworld()







# def my_decorator(my_function):    # <-- (4)
#     def inner_decorator():        # <-- (5)
#         print("This happened before!")  # <-- (6)
#         my_function()             # <-- (7)
#         print("This happens after ")    # <-- (10)
#         print("This happened at the end!")    # <-- (11)
#     return inner_decorator
#     # return None

# @my_decorator       # <-- (3)
# def my_decorated():    # <-- (2) <-- (8)
#     print("This happened!")   # <-- (9)


# def cap_decorator(func):
#     def wrapper(name):
#         name = name.capitalize()
#         func(name)
#     return wrapper

# @cap_decorator
# def print_my_name(name):
#     print("Hello world from",name)

# @cap_decorator
# def say_hello_to_me(name):
#     print("Hello to",name)

# print_my_name("eyal")
# say_hello_to_me("eyal")

def cap_decorator(func):
    def wrapper(*args, **kwargs):
        args = [arg.capitalize() for arg in args]
        func(*args, **kwargs)
    return wrapper

@cap_decorator
def describe_me(first_name, last_name, favourite_activity):
    print("I am {} {} and I love {}".format(first_name, last_name, favourite_activity))

@cap_decorator
def describe_my_family(father_name, mother_name, brother_name, sister_name):
    print("The name of my father is", father_name)
    print("The name of my mother is", mother_name)
    print("The name of my brother is", brother_name)
    print("The name of my sister is", sister_name)

describe_me("Alexis", "Monster", "coding")
describe_my_family("John","Valentina","mario","luigi")
