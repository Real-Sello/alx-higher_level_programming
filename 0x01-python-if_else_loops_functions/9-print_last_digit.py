#!/usr/bin/python3

# print_last_digit: prints last digit of any number
# Number: arguments that hold pass values
# last: holds last digit of passed argument
# Return: Last digit value

def print_last_digit(number):
    if number < 0:
        last = (-1 * number) % 10

    else:
        last = number % 10

    print('{}'.format(last), end='')

    return last
