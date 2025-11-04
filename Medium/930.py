class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 使用前缀和与哈希表统计子数组个数
        prefix_sum_count = {0: 1}  # 存储前缀和出现次数，初始前缀和0出现1次
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num  # 更新当前前缀和
            # 如果存在前缀和等于current_sum - goal，说明存在子数组和为goal
            if current_sum - goal in prefix_sum_count:
                count += prefix_sum_count[current_sum - goal]
            # 更新当前前缀和的出现次数
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count
