class MinStack:
    def __init__(self):
        # 主栈存储所有元素
        self.stack = []
        # 辅助栈存储当前最小值
        self.min_stack = []

    def push(self, val: int) -> None:
        # 将元素压入主栈
        self.stack.append(val)
        # 如果辅助栈为空或新值小于等于当前最小值，压入辅助栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 如果主栈栈顶元素等于辅助栈栈顶元素，同时弹出辅助栈
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        # 弹出主栈栈顶元素
        self.stack.pop()

    def top(self) -> int:
        # 返回主栈栈顶元素
        return self.stack[-1]

    def getMin(self) -> int:
        # 返回辅助栈栈顶元素，即当前最小值
        return self.min_stack[-1]
