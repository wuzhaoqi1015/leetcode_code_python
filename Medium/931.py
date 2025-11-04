class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 使用动态规划，dp[i][j]表示到达(i,j)位置的最小路径和
        dp = [[0] * n for _ in range(n)]
        
        # 初始化第一行
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # 从第二行开始计算
        for i in range(1, n):
            for j in range(n):
                # 当前位置的最小路径和等于当前值加上上一行可到达位置的最小值
                # 考虑三个可能的上方位置：左上、正上、右上
                min_prev = dp[i-1][j]  # 正上方
                if j > 0:
                    min_prev = min(min_prev, dp[i-1][j-1])  # 左上方
                if j < n - 1:
                    min_prev = min(min_prev, dp[i-1][j+1])  # 右上方
                dp[i][j] = matrix[i][j] + min_prev
        
        # 返回最后一行中的最小值
        return min(dp[n-1])
