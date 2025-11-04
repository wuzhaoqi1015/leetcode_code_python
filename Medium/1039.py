class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j]表示从顶点i到顶点j（包含）构成的多边形的最小三角剖分分数
        dp = [[0] * n for _ in range(n)]
        
        # 从长度为3的多边形开始（三角形）
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                # 尝试所有可能的三角形划分，以k为中间顶点
                for k in range(i + 1, j):
                    # 计算当前划分的分数：三角形(i,k,j)的乘积 + 左右两个多边形的分数
                    current_score = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], current_score)
        
        return dp[0][n - 1]
