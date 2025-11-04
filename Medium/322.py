class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp数组，dp[i]表示凑成金额i所需的最少硬币数
        # 初始值设为amount+1，这是一个不可能达到的较大值
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 金额为0时不需要任何硬币
        
        # 遍历所有金额从1到amount
        for i in range(1, amount + 1):
            # 遍历所有硬币面额
            for coin in coins:
                # 如果当前金额大于等于硬币面额
                if i >= coin:
                    # 更新dp[i]为min(当前值, 使用这枚硬币后的硬币数+1)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 如果dp[amount]仍然为初始值，说明无法凑出该金额
        return dp[amount] if dp[amount] != amount + 1 else -1
