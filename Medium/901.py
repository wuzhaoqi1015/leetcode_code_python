class StockSpanner:

    def __init__(self):
        # 使用栈来存储(价格, 跨度)元组
        self.stack = []

    def next(self, price: int) -> int:
        # 初始跨度为1（包含当天）
        span = 1
        
        # 当栈不为空且栈顶价格小于等于当前价格时
        while self.stack and self.stack[-1][0] <= price:
            # 弹出栈顶元素并将其跨度累加到当前跨度
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        
        # 将当前价格和计算出的跨度压入栈中
        self.stack.append((price, span))
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
