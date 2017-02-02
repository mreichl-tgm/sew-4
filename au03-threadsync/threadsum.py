import random
import threading
import time
import math


class ThreadSum(threading.Thread):
    total = 0
    lock = threading.Lock()

    def __init__(self, n1, n2):
        """
        Used to calculate the sum of all numbers between n1 and n2
        Results are later saved in:
        - number
        - thread_count
        - result
        - time

        :param n1: int
        :param n2: int
        """
        super().__init__()
        self.n1 = n1
        self.n2 = n2

    def run(self):
        """
        Overrides run to add iterate over all numbers between n1 and n2 and add them to class total when done
        """
        total = 0

        for i in range(self.n1, self.n2):
            total += i

        with ThreadSum.lock:
            ThreadSum.total += total


class Sum:
    def __init__(self, number, thread_count):
        """
        Splits the number into a given number of threads and add the pisces sum to a total result.
        Also uses a StopWatch to measure the time used for this process.

        :param number: int
        :param thread_count: int
        """
        number = number
        thread_count = thread_count

        threads = []

        part = number / thread_count

        with ThreadSum.lock:
            ThreadSum.total = 0
        # Starting Time
        t1 = time.time()

        for i in range(thread_count):
            start = part * i
            end = start + part

            thread = ThreadSum(math.ceil(start), math.ceil(end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        # End Time
        t2 = time.time()

        self.number = number
        self.thread_count = thread_count
        self.result = ThreadSum.total
        self.time = (t2 - t1) * 10 ** 6


class ThreadSumWriter:
    def __init__(self, nmin=10**5, nmax=10**6, tmin=1, tmax=20, iterations=10):
        """
        Writes a Sum object to a file using the csv format

        :param nmin: int
        :param nmax: int
        :param tmin: int
        :param tmax: int
        :param iterations: int
        """
        f = open('stats.csv', 'w+')
        print("Created file: " + f.name)

        f.write("number, result, threads, time\n")

        rand = random.randint(nmin, nmax)
        for i in range(tmin, tmax):
            total_time = 0
            for j in range(iterations):
                s = Sum(rand, i)
                total_time += s.time

            f.write(
                str(s.number) + ", " +
                str(s.result) + ", " +
                str(i) + ", " +
                str(total_time / iterations) + "\n")

        f.close()

tsw = ThreadSumWriter()
