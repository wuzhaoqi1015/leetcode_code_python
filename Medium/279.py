class Solution:
    def numSquares(self, n: int) -> int:
        # 使用动态规划求解
        # dp[i]表示和为i的完全平方数的最少数量
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 初始状态：和为0需要0个完全平方数
        
        # 遍历所有可能的和
        for i in range(1, n + 1):
            # 遍历所有可能的完全平方数
            j = 1
            while j * j <= i:
                # 状态转移方程：dp[i] = min(dp[i], dp[i - j*j] + 1)
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]
