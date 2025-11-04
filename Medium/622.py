class MyCircularQueue:

    def __init__(self, k: int):
        # 初始化队列，大小为k+1，多一个位置用于区分空和满的状态
        self.queue = [0] * (k + 1)
        self.front = 0  # 队首指针
        self.rear = 0   # 队尾指针
        self.capacity = k + 1  # 队列容量

    def enQueue(self, value: int) -> bool:
        # 如果队列已满，返回False
        if self.isFull():
            return False
        # 在队尾插入元素
        self.queue[self.rear] = value
        # 队尾指针循环移动
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        # 如果队列为空，返回False
        if self.isEmpty():
            return False
        # 队首指针循环移动，实现出队
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        # 如果队列为空，返回-1
        if self.isEmpty():
            return -1
        # 返回队首元素
        return self.queue[self.front]

    def Rear(self) -> int:
        # 如果队列为空，返回-1
        if self.isEmpty():
            return -1
        # 返回队尾元素，注意rear指向的是下一个插入位置，需要取前一个位置
        return self.queue[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        # 队首和队尾指针相同时队列为空
        return self.front == self.rear

    def isFull(self) -> bool:
        # 队尾指针的下一个位置是队首时队列为满
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
