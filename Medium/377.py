class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 使用动态规划，dp[i]表示总和为i的组合个数
        dp = [0] * (target + 1)
        dp[0] = 1  # 总和为0只有一种组合：空组合
        
        # 遍历所有可能的总和值
        for i in range(1, target + 1):
            # 对于每个总和i，遍历所有可能的数字选择
            for num in nums:
                # 如果当前数字小于等于当前目标值
                if num <= i:
                    # 累加使用当前数字的组合数
                    dp[i] += dp[i - num]
        
        return dp[target]
