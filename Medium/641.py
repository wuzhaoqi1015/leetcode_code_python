class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k  # 队列容量
        self.size = 0      # 当前队列大小
        self.front = 0     # 队列头部指针
        self.rear = 0      # 队列尾部指针
        self.data = [0] * k  # 固定大小的数组存储数据

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # 在头部插入元素，需要前移front指针
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # 在尾部插入元素
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # 删除头部元素，后移front指针
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # 删除尾部元素，前移rear指针
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # rear指向的是下一个插入位置，需要获取前一个位置的元素
        return self.data[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
