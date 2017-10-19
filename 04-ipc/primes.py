import queue
import threading


class PrimeProducer(threading.Thread):
    def __init__(self, q, e):
        """
        Puts all primes it finds into a queue and breaks on event trigger

        :param q: queue.Queue
        :param e: threading.Event
        """
        super().__init__()
        self.q = q
        self.e = e
        self.n = 2

    def run(self):
        while not self.e.is_set():
            self.n += 1
            prime = True
            for i in range(2, int(self.n / 2) + 2):
                if self.n % i == 0:
                    prime = False

            if prime:
                self.q.put(self.n)


class PrimeConsumer(threading.Thread):
    def __init__(self, q, f, e):
        """
        Fetches primes from a queue and writes them to a file. Breaks on event trigger.

        :param q: queue.Queue
        :param f: File
        :param e: threading.Event
        """
        super().__init__()
        self.q = q
        self.f = f
        self.e = e

    def run(self):
        while not self.e.is_set():
            n = self.q.get()
            self.f.write(str(n) + "\n")


class PrimeUI(threading.Thread):
    def __init__(self, pp, q, e):
        """
        A basic user interface to verbose and quit the prime production

        :param pp: PrimeProducer
        :param q: queue.Queue
        :param e: threading.Event
        """
        super().__init__()
        self.pp = pp
        self.q = q
        self.e = e

    def run(self):
        while True:
            mode = input("Quit or Verbose? (q, v)")
            if mode == "v":
                print(self.pp.n)
            if mode == "q":
                self.e.set()
                return


class PrimeFactory:
    def __init__(self):
        """
        Instantiates exactly 1 queue, event, PrimeProducer, PrimeConsumer, PrimeUI and starts them.
        """
        f = open("primes.txt", "w+")
        q = queue.Queue()
        # Event used to stop the threads
        e = threading.Event()
        # Create Threads
        pp = PrimeProducer(q, e)
        pc = PrimeConsumer(q, f, e)
        pi = PrimeUI(pp, q, e)
        # Start Threads
        pi.start()
        pp.start()
        pc.start()
        # Join Threads
        pi.join()
        pp.join()
        pc.join()

        f.close()

if __name__ == '__main__':
    pf = PrimeFactory()
