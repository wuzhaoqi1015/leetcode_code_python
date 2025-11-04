class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 使用动态规划，dp[i][j]表示在区间[i,j]内确保获胜的最小现金数
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # 从区间长度2开始遍历，因为长度为1时不需要花费
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                # 初始化为一个很大的值
                dp[start][end] = float('inf')
                # 遍历所有可能的猜测点
                for k in range(start, end):
                    # 当前猜测的花费为k加上左右区间中较大的花费
                    cost = k + max(dp[start][k - 1], dp[k + 1][end])
                    # 取所有猜测中的最小值
                    if cost < dp[start][end]:
                        dp[start][end] = cost
        
        # 返回整个区间[1,n]的最小花费
        return dp[1][n]
