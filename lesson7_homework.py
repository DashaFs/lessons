# def my_map_func(func, iterable):
#     list =[]
#     for i in iterable:
#         list.append(func(i))
#     print(list)
#
#
# def square(x):
#     return x ** 2
#
#
# list_1 = [1, 3, 4, 5, 6]
#
# # with a function
# my_map_func(square, list_1)
#
# # with lambda
# my_map_func(lambda x: x**2, list_1)
#
# def my_filter_func(func, iterable):
#     filtered_list = []
#     for item in iterable:
#         if func(item):
#             filtered_list.append(item)
#     print(filtered_list)
#
# my_filter_func(lambda x: x%2==0, list_1)


#task2

# def create_lambda(x):
#     return lambda y : y**x
#
# function = create_lambda(3)
# result = function(2)
# print(result)


#task3
def print_smt():
    return "Hello, world!"


def calc():
    return 2 + 2


def execute_function(func_name):
    my_functions = {'print_smt': print_smt,'calc': calc}
    if func_name in my_functions:
        func = my_functions[func_name]
        result = func()
        print(f"Result of {func_name} {result}")
    else:
        print(f"Function {func_name} does not exist in your list of functions.")


func_name = input("Enter the name of the function: ")
execute_function(func_name)

