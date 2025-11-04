class Solution:
    def minSteps(self, n: int) -> int:
        # 如果n为1，不需要任何操作
        if n == 1:
            return 0
        
        # 初始化dp数组，dp[i]表示得到i个'A'所需的最小操作次数
        dp = [float('inf')] * (n + 1)
        dp[1] = 0  # 初始状态已有1个'A'
        
        # 动态规划求解
        for i in range(2, n + 1):
            # 寻找i的最大因子j，通过复制j个'A'然后粘贴来得到i个'A'
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    # 通过因子j得到i
                    dp[i] = min(dp[i], dp[j] + i // j)
                    # 通过另一个因子i//j得到i
                    dp[i] = min(dp[i], dp[i // j] + j)
        
        return dp[n]
