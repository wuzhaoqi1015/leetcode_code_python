class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度
        dp = [1] * n
        # count[i] 表示以 nums[i] 结尾的最长递增子序列的个数
        count = [1] * n
        
        max_len = 1  # 记录全局最长递增子序列的长度
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 找到更长的递增子序列
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]  # 重新计数
                    # 找到相同长度的递增子序列
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]  # 累加个数
            
            # 更新全局最长长度
            if dp[i] > max_len:
                max_len = dp[i]
        
        # 统计所有达到最长长度的序列个数
        result = 0
        for i in range(n):
            if dp[i] == max_len:
                result += count[i]
                
        return result
