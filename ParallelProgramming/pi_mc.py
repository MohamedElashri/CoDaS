import math
import multiprocessing
import random
import time
from logging import raiseExceptions
from signal import raise_signal

random.seed(42)


def mc(n: int) -> int:
    """
    This function is used to calculate the value of pi
    :param n: the number of points
    :return: the value of pi
    """
    cout = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) <= 1:
            cout += 1
    return cout


def main() -> None:
    """
    The main function to call multiprocessing routine.
    """
    n_steps = int(1e7)
    n_cpu = multiprocessing.cpu_count()
    print("Number of CPUs is: {}".format(n_cpu))
    n_processes = 4  # Assign number of processes to use
    # if n_processes is 0, then it will use the default number of processes
    if n_processes == 0:
        n_processes = n_cpu
    print("Number of processes to use is: {}".format(n_processes))
    start = time.time()
    pool = multiprocessing.Pool(n_processes)
    mp = pool.map(mc, [n_steps] * n_processes)
    pi = 4 * sum(mp) / (n_steps * n_processes)
    end = time.time()
    print("Pi Estimation is: {}".format(pi))
    print("Time it took (in seconds) is: {}".format(end - start))


if __name__ == "__main__":
    main()
