class RecentCounter:

    def __init__(self):
        # 使用队列存储请求时间
        self.queue = []

    def ping(self, t: int) -> int:
        # 将当前请求时间加入队列
        self.queue.append(t)
        # 计算时间范围下限
        lower_bound = t - 3000
        # 移除所有不在时间范围内的早期请求
        while self.queue and self.queue[0] < lower_bound:
            self.queue.pop(0)
        # 返回队列中剩余请求的数量
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
