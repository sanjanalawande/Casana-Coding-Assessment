import sys
from colorama import Fore, Style


def fib(curr_value, prev_value, count, n=4):
    """
    Function to Print the next element of Fibonacci sequence recursively
    """
    if count < int(sys.argv[1]) and curr_value <= n:
        count = count + 1

        print(curr_value)

        return fib(curr_value + prev_value, curr_value, count, n)


def main(n):
    """
    :param n: 144
    :return: The Fibonacci Series
    Function to Print the Fibonacci sequence and call the fib function
    """
    print(f"This is the {Fore.GREEN}Fibonacci{Style.RESET_ALL} Sequence!")
    print(f"Number of values in the Fibonacci sequence = {int(sys.argv[1])}")

    # count to keep track of the number of values of the Fibonacci Series displayed
    count = 0
    fib(0, 1, count, n)


if __name__ == '__main__':
    main(144)
