class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 计算从0到n的期望总和，然后减去数组中所有数字的实际总和
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # 0到n的连续整数和公式
        actual_sum = sum(nums)
        return expected_sum - actual_sum
