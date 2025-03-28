
# Standard Library
from sys import argv

# Local Library
from cfc import *


def sign(number):
    return True if number > 0 else False


if __name__ == '__main__':

    precision = int(argv[argv.index('-p') + 1]) if '-p' in argv else 2
    lower_boundary = float(argv[argv.index('-l') + 1]) / 100 if '-l' in argv else pow(10, -10)
    upper_boundary = float(argv[argv.index('-u') + 1]) / 100 if '-u' in argv else 1

    def equation(i): return eval(argv[1])

    while True:

        center_of_interval = (lower_boundary + upper_boundary) / 2
        if sign(equation(lower_boundary)) != sign(equation(center_of_interval)):
            upper_boundary = center_of_interval
        elif sign(equation(upper_boundary)) != sign(equation(center_of_interval)):
            lower_boundary = center_of_interval
        else:
            print(f'({lower_boundary * 100}%, {upper_boundary * 100}%): No solution in the interval')
            break

        if upper_boundary - lower_boundary <= pow(10, -1 * precision - 2):
            print(f'Rate of Return: {round(center_of_interval * 100, precision)}%')
            break
