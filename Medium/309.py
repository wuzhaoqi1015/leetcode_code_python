class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        # 定义三种状态：
        # dp[i][0]: 第i天结束时持有股票的最大利润
        # dp[i][1]: 第i天结束时不持有股票且处于冷冻期的最大利润
        # dp[i][2]: 第i天结束时不持有股票且不处于冷冻期的最大利润
        
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]  # 第一天买入股票
        dp[0][1] = 0           # 第一天不可能处于冷冻期
        dp[0][2] = 0           # 第一天不持有股票且不处于冷冻期
        
        for i in range(1, n):
            # 第i天持有股票：可能是i-1天就持有，或者i-1天不持有且不处于冷冻期时买入
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            # 第i天处于冷冻期：只能是i-1天卖出股票（即i-1天持有股票并在i天卖出）
            dp[i][1] = dp[i-1][0] + prices[i]
            # 第i天不持有股票且不处于冷冻期：可能是i-1天就不持有股票（冷冻期或非冷冻期）
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        # 最大利润出现在最后一天不持有股票的状态（可能是冷冻期或非冷冻期）
        return max(dp[n-1][1], dp[n-1][2])
