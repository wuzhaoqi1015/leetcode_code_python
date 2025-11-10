class Solution:
    def fib(self, n: int) -> int:
        # 处理边界情况
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # 使用动态规划，只保存前两个值
        prev1, prev2 = 0, 1
        
        # 从2开始计算到n
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2
