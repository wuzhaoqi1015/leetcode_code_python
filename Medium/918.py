class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 处理数组长度为1的特殊情况
        if len(nums) == 1:
            return nums[0]
        
        # 计算普通数组的最大子数组和（Kadane算法）
        max_current = nums[0]
        max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
        
        # 计算普通数组的最小子数组和
        min_current = nums[0]
        min_global = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            min_current = min(nums[i], min_current + nums[i])
            min_global = min(min_global, min_current)
            total += nums[i]
        
        # 环形数组的最大子数组和有两种情况：
        # 1. 普通数组的最大子数组和（不跨越边界）
        # 2. 总和减去最小子数组和（跨越边界的情况）
        # 如果所有数都是负数，则最大子数组和就是普通数组的最大子数组和
        if total == min_global:
            return max_global
        else:
            return max(max_global, total - min_global)
