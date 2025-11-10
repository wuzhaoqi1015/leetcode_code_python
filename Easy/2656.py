class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # 找到数组中的最大值
        max_num = max(nums)
        # 计算从max_num开始的k个连续整数的和
        # 使用等差数列求和公式：首项为max_num，末项为max_num + k - 1
        total = (max_num + (max_num + k - 1)) * k // 2
        return total
