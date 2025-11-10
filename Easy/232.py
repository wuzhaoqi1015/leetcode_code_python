class MyQueue:
    def __init__(self):
        # 使用两个栈，s1用于入队操作，s2用于出队操作
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # 直接将新元素压入s1栈
        self.s1.append(x)

    def pop(self) -> int:
        # 如果s2为空，需要将s1中的所有元素转移到s2中
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # 从s2栈顶弹出元素，即队列头部元素
        return self.s2.pop()

    def peek(self) -> int:
        # 如果s2为空，需要将s1中的所有元素转移到s2中
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # 返回s2栈顶元素，即队列头部元素，但不弹出
        return self.s2[-1]

    def empty(self) -> bool:
        # 当两个栈都为空时，队列为空
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
