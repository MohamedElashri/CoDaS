# Tiny script to estimate the value of pi using the Bailey-Borwein-Plouffe formula
# Mohamed Elashri
# 04/08/2022


from multiprocessing import pool
import random
import multiprocessing
from multiprocessing import Pool


# Multiprocessing based code to estimate the value of PI using
# Bailey-Borwein-Plouffe formula

from decimal import Decimal, getcontext
from timeit import default_timer as timer
from multiprocessing import Pool, current_process
import time


def pi(p: int) -> Decimal:
    """
    Calculate pi to the specified number of digits using the
    Bailey-Borwein-Plouffe formula.

    :param p: The number of digits after the decimal point.
    :return: The value of pi as a Decimal.
    """
    getcontext().prec = p
    return sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) -
                                   Decimal(2)/(8*k+4) -
                                   Decimal(1)/(8*k+5) -
                                   Decimal(1)/(8*k+6)) for k in range(p))


def main() -> None:
    """
    This is a multi-line Google style docstring.

    Args:
        None

    Returns:
        None
    """

    start = timer()

    with Pool(3) as pool:
        results = pool.map(pi, range(1, 10))
        #print(results)
        print("Pi Estimation is: {}".format(results))

    end = timer()
    print("Time taken: ", end-start)


if __name__ == '__main__':
    main()