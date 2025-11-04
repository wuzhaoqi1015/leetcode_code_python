MOD = 10**9 + 7

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 计算单个数组的最大子数组和（Kadane算法）
        def kadane(nums):
            max_sum = current_sum = 0
            for num in nums:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        
        # 计算整个数组的和
        total_sum = sum(arr)
        
        # 如果k为1，直接返回单个数组的最大子数组和
        if k == 1:
            return kadane(arr) % MOD
        
        # 计算两个数组连接后的最大子数组和
        double_arr = arr * 2
        double_max = kadane(double_arr)
        
        # 如果整个数组的和为正数，考虑中间重复部分
        if total_sum > 0:
            # 最大子数组和 = 两个数组连接的最大子数组和 + (k-2) * 整个数组的和
            result = double_max + (k - 2) * total_sum
            return result % MOD
        else:
            # 如果整个数组的和非正，最大子数组和不会超过两个数组连接的情况
            return double_max % MOD
