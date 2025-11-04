import threading

class DiningPhilosophers:
    def __init__(self):
        # 初始化5把叉子的锁，对应0-4号哲学家
        self.forks = [threading.Lock() for _ in range(5)]
        # 全局锁，确保同时只有一位哲学家尝试拿叉子，避免死锁
        self.global_lock = threading.Lock()

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # 计算左右叉子的索引
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        # 使用全局锁确保同时只有一位哲学家尝试拿叉子
        with self.global_lock:
            # 获取左右叉子
            self.forks[left_fork].acquire()
            self.forks[right_fork].acquire()

        # 拿起左右叉子
        pickLeftFork()
        pickRightFork()

        # 进餐
        eat()

        # 放下左右叉子
        putLeftFork()
        putRightFork()

        # 释放左右叉子的锁
        self.forks[left_fork].release()
        self.forks[right_fork].release()
