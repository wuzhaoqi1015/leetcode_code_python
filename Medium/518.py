class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 初始化动态规划数组，dp[i]表示金额为i时的组合数
        dp = [0] * (amount + 1)
        # 金额为0时只有一种组合方式：不选任何硬币
        dp[0] = 1
        
        # 遍历每种硬币
        for coin in coins:
            # 从当前硬币面值开始遍历到目标金额
            for i in range(coin, amount + 1):
                # 累加使用当前硬币的组合数
                dp[i] += dp[i - coin]
        
        return dp[amount]
