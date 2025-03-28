
# Standard Library
from sys import argv

# Local Library
from cfc import *


if __name__ == '__main__':

    precision = int(argv[argv.index('-p') + 1]) if '-p' in argv else 2
    result = eval(argv[1])
    print(round(result, precision))

