class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化当前子数组和与最大子数组和
        current_sum = nums[0]
        max_sum = nums[0]
        
        # 遍历数组，从第二个元素开始
        for i in range(1, len(nums)):
            # 如果当前子数组和为负，则重新开始计算
            if current_sum < 0:
                current_sum = nums[i]
            else:
                # 否则继续累加当前元素
                current_sum += nums[i]
            
            # 更新最大子数组和
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum
