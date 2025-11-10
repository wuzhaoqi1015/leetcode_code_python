from threading import Lock

class Foo:
    def __init__(self):
        # 初始化两个锁，分别用于控制second和third的执行顺序
        self.first_done = Lock()
        self.second_done = Lock()
        # 立即获取这两个锁，使得second和third方法在开始时被阻塞
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # 释放first_done锁，允许second方法执行
        self.first_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # 等待first方法完成
        self.first_done.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # 释放second_done锁，允许third方法执行
        self.second_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # 等待second方法完成
        self.second_done.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
