class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 生成不超过k的斐波那契数列
        fib = [1, 1]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
        
        count = 0
        remaining = k
        # 从最大的斐波那契数开始贪心选择
        for num in reversed(fib):
            if remaining >= num:
                remaining -= num
                count += 1
            if remaining == 0:
                break
        return count
