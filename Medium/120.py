class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # 使用一维数组存储当前行的最小路径和
        dp = [0] * n
        # 初始化最后一行的值
        for i in range(n):
            dp[i] = triangle[n-1][i]
        # 从倒数第二行开始向上递推
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                # 状态转移方程：当前位置的最小路径和等于当前值加上下一行相邻两个位置中较小的值
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
