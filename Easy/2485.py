class Solution:
    def pivotInteger(self, n: int) -> int:
        # 计算总和
        total_sum = n * (n + 1) // 2
        # 遍历可能的x值
        for x in range(1, n + 1):
            # 计算1到x的和
            left_sum = x * (x + 1) // 2
            # 计算x到n的和 = 总和 - 1到x-1的和
            right_sum = total_sum - left_sum + x
            # 检查是否满足条件
            if left_sum == right_sum:
                return x
        return -1
