class Solution:
    def tribonacci(self, n: int) -> int:
        # 处理特殊情况
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # 初始化前三个泰波那契数
        t0, t1, t2 = 0, 1, 1
        
        # 从第3个数开始计算到第n个数
        for i in range(3, n + 1):
            # 计算当前泰波那契数
            current = t0 + t1 + t2
            # 更新前三个数的值
            t0, t1, t2 = t1, t2, current
        
        # 返回第n个泰波那契数
        return t2
