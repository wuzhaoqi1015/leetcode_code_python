class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 初始化dp数组，大小与grid相同
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # 初始化第一列，只能从上方移动下来
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 初始化第一行，只能从左方移动过来
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 填充剩余dp数组
        for i in range(1, m):
            for j in range(1, n):
                # 当前位置的最小路径和等于上方和左方较小值加上当前格子的值
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
