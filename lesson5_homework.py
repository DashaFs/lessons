#
# import math
#
#
# #task1
# class NegativeNumberError(Exception):
#     pass
#
# def square_root():
#     try:
#         number = int(input('Please enter a number:'))
#         if number < 0:
#             raise NegativeNumberError('Cannot compute square root of a negative number')
#         else:
#             result = math.sqrt(number)
#             print(f'Square root of {number} is {result}')
#     except NegativeNumberError as e:
#         print(e)
#     finally:
#         print('Thanks, the operation is finished')
#
# square_root()
#
# #task2
#
# class NegativeNumberError(Exception):
#     pass
#
# def square_root():
#     try:
#         number = int(input('Please enter a number:'))
#         if number < 0:
#             raise NegativeNumberError('Cannot compute square root of a negative number')
#         else:
#             result = math.sqrt(number)
#             print(f'Square root of {number} is {result}')
#     except NegativeNumberError as e:
#         print(e)
#     except ValueError:
#         print("Please enter a valid format.")
#     finally:
#         print('Thanks, the operation is finished')
#
# square_root()

#task3
def calc():
    while True:
        try:
            num_1 = input("Enter the first number or type 'exit' to quit: ")
            if num_1 == "exit":
                break
            num_1 = int(num_1)

            num_2 = input("Enter the second number or type 'exit' to quit: ")
            if num_2 == "exit":
                break
            num_2 = int(num_2)

            operator  = input('Enter operation: "+", "-", "/", "*" (or type "exit" to quit):')
            if operator == "exit":
                break

            if operator == "+":
                print(num_1 + num_2)
            elif operator == "-":
                print(num_1 - num_2)
            elif operator == "/":
                try:
                    num_1/num_2
                except ZeroDivisionError:
                    print('Can not divide by zero!')

            elif operator == "*":
                print(num_1 * num_2)
            else:
                print("Invalid operation. Please try again.")

        except ValueError:
             print("Error: Invalid input! Please enter a valid number.")

        except Exception as e:
            print("An unexpected error occurred:", e)

        else:
            print("Calculation completed successfully.")

        finally:
            print("Bye")

calc()













