class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for m in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[m][j - 1] + (prefix[i] - prefix[m]) / (i - m))
        
        return dp[n][k]
