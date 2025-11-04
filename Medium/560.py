class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 使用哈希表记录前缀和出现的次数
        prefix_sum_count = {0: 1}  # 初始化前缀和为0出现1次
        current_sum = 0
        count = 0
        
        # 遍历数组计算前缀和
        for num in nums:
            current_sum += num  # 更新当前前缀和
            
            # 如果存在前缀和等于current_sum - k，说明存在子数组和为k
            if current_sum - k in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            # 更新当前前缀和出现的次数
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return count
