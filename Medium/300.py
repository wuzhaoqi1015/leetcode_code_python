class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 使用动态规划方法，dp[i]表示以nums[i]结尾的最长递增子序列长度
        n = len(nums)
        if n == 0:
            return 0
            
        dp = [1] * n  # 初始化dp数组，每个位置至少长度为1
        
        # 遍历数组，计算每个位置的最长递增子序列长度
        for i in range(n):
            for j in range(i):
                # 如果当前元素大于前面的元素，可以形成更长的递增子序列
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # 返回dp数组中的最大值
        return max(dp)
