MOD = 10**9 + 7

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 如果目标值小于骰子数量或大于最大可能值，直接返回0
        if target < n or target > n * k:
            return 0
        
        # 初始化动态规划数组，dp[i][j]表示使用i个骰子得到总和j的方法数
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # 初始化：0个骰子得到总和0的方法数为1
        dp[0][0] = 1
        
        # 遍历骰子数量
        for i in range(1, n + 1):
            # 遍历可能的总和值
            for j in range(i, min(i * k, target) + 1):
                # 遍历当前骰子可能的值
                for face in range(1, k + 1):
                    if j - face >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD
        
        return dp[n][target]
