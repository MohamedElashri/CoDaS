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


def pi(p):
    getcontext().prec = p
    # return Bailey-Borwein-Plouffe formula
    return sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) -
                                   Decimal(2)/(8*k+4) -
                                   Decimal(1)/(8*k+5) -
                                   Decimal(1)/(8*k+6)) for k in range(p))


def main():

    start = timer()

    with Pool(3) as pool:
        results = pool.map(pi, range(1, 10))
        print(results)

    end = timer()
    print("Time taken: ", end-start)


if __name__ == '__main__':
    main()
