from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 5 == 0 and self.current % 3 != 0:
                    printBuzz()
                    self.current += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 == 0 and self.current % 5 == 0:
                    printFizzBuzz()
                    self.current += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1
