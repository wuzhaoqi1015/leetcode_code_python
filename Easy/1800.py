class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 初始化当前子数组和与最大子数组和
        current_sum = nums[0]
        max_sum = nums[0]
        
        # 遍历数组，从第二个元素开始
        for i in range(1, len(nums)):
            # 如果当前元素大于前一个元素，则继续累加当前子数组
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                # 否则重置当前子数组和为当前元素值
                current_sum = nums[i]
            
            # 更新最大子数组和
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum
