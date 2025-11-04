class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []  # 使用列表存储栈元素
        self.max_size = maxSize  # 栈的最大容量

    def push(self, x: int) -> None:
        # 如果栈未满，则添加元素到栈顶
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        # 如果栈不为空，弹出并返回栈顶元素；否则返回-1
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        # 对栈底k个元素增加val，如果元素数量小于k则全部增加
        n = min(k, len(self.stack))
        for i in range(n):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
