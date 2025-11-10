class Solution:
    def divisorGame(self, n: int) -> bool:
        # 使用动态规划，dp[i]表示当数字为i时先手玩家是否能获胜
        dp = [False] * (n + 1)
        # 从2开始计算，因为n=1时无法操作直接输
        for i in range(2, n + 1):
            # 遍历所有可能的除数x
            for x in range(1, i):
                # 如果x是i的因数且对手在i-x时无法获胜，则当前玩家获胜
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]
