class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 使用哈希表存储前缀和第一次出现的位置
        prefix_map = {0: -1}  # 初始化前缀和为0的位置为-1
        max_length = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            # 将0视为-1，1视为1，这样相同数量的0和1对应前缀和为0
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            # 如果当前前缀和之前出现过，说明中间段的和为0
            if prefix_sum in prefix_map:
                # 计算当前子数组长度
                current_length = i - prefix_map[prefix_sum]
                max_length = max(max_length, current_length)
            else:
                # 记录前缀和第一次出现的位置
                prefix_map[prefix_sum] = i
        
        return max_length
