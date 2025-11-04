class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 使用前缀和与哈希表来统计优美子数组数量
        # 将奇数视为1，偶数视为0，问题转化为求和为k的子数组个数
        count = 0
        prefix_sum = 0
        # 哈希表存储前缀和出现的次数，初始时前缀和为0出现1次
        prefix_count = {0: 1}
        
        for num in nums:
            # 当前数字如果是奇数，前缀和加1，否则加0
            prefix_sum += num % 2
            
            # 如果存在前缀和为prefix_sum - k，说明找到了满足条件的子数组
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            # 更新当前前缀和的出现次数
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
                
        return count
