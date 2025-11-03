class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建动态规划数组，dp[i][j]表示到达(i,j)位置的路径数
        dp = [[0] * n for _ in range(m)]
        
        # 初始化第一行和第一列，因为只能向右或向下移动
        # 第一行的所有位置都只有1条路径（一直向右）
        for i in range(m):
            dp[i][0] = 1
        # 第一列的所有位置都只有1条路径（一直向下）
        for j in range(n):
            dp[0][j] = 1
        
        # 填充剩余的网格位置
        # 每个位置的路径数等于上方位置和左方位置的路径数之和
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 返回右下角位置的路径数
        return dp[m-1][n-1]
