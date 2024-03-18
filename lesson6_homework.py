import math

# task


def sum_range():
    try:
        start = int(input('Enter the first number: '))
        end = int(input('Enter the second number: '))
        if start > end:
            start, end = end, start
        if start < 0 or end < 0:
            raise ValueError("Negative numbers are not allowed")
        count = 0
        for num in range(start, end):
            count += num
        print(f"Sum of numbers in the range {count}")
    except ValueError as e:
        print(e)


sum_range()

# task2


def sqr():
    side = int(input('Enter the side: '))
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    print(f"The perimeter is {perimeter}, the area is {area}, the diagonal is {diagonal}")


sqr()


# task3

def get_user_input():
    user_input = input("Enter data: ")
    return user_input


def print_data_type(data):
    try:
        evaluated_data = eval(data)
        data_type = type(evaluated_data)
        print(f"User is going to work with {data_type}")
    except NameError as ne:
        print(f"Error: {ne}")


data = get_user_input()
print_data_type(data)
