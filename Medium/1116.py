from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock.acquire()
        self.odd_lock.acquire()
        self.current = 1
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            if self.current % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.current += 1
            self.zero_lock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.current += 1
            self.zero_lock.release()
