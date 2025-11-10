from collections import deque

class MyStack:

    def __init__(self):
        # 使用两个队列，q1是主队列，q2是辅助队列
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # 将新元素先加入辅助队列q2
        self.q2.append(x)
        # 将q1中的所有元素依次出队并加入q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # 交换q1和q2，使得q1始终是主队列
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # 直接从q1中弹出队首元素（即栈顶元素）
        return self.q1.popleft()

    def top(self) -> int:
        # 返回q1的队首元素（即栈顶元素）
        return self.q1[0]

    def empty(self) -> bool:
        # 检查q1是否为空
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
