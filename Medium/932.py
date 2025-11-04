class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # 使用分治思想构建漂亮数组
        # 漂亮数组的性质：如果A是漂亮数组，那么将A中每个元素乘以2-1（奇数映射）和乘以2（偶数映射）后仍然是漂亮数组
        memo = {1: [1]}  # 备忘录，存储已计算的漂亮数组
        
        def f(n):
            if n not in memo:
                # 分别构建左半部分（奇数）和右半部分（偶数）
                left = f((n + 1) // 2)  # 左半部分长度为(n+1)//2
                right = f(n // 2)       # 右半部分长度为n//2
                # 将左半部分映射为奇数，右半部分映射为偶数
                memo[n] = [2 * x - 1 for x in left] + [2 * x for x in right]
            return memo[n]
        
        return f(n)
