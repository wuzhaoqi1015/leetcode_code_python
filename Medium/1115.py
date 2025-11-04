from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()  # 初始时bar锁被占用，确保foo先执行

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()  # 获取foo锁
            printFoo()
            self.bar_lock.release()  # 释放bar锁，允许bar执行

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()  # 获取bar锁
            printBar()
            self.foo_lock.release()  # 释放foo锁，允许foo执行
