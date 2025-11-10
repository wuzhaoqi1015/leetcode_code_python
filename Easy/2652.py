class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        # 遍历从1到n的所有整数
        for num in range(1, n + 1):
            # 检查当前数字是否能被3、5或7整除
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                total_sum += num
        return total_sum
