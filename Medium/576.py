MOD = 10**9 + 7
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 使用动态规划，dp[k][i][j]表示移动k次后位于(i,j)的路径数
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1  # 初始位置
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 四个移动方向
        result = 0
        
        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if dp[k][i][j] > 0:  # 当前位置有路径
                        for dx, dy in directions:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < m and 0 <= nj < n:  # 仍在网格内
                                dp[k + 1][ni][nj] = (dp[k + 1][ni][nj] + dp[k][i][j]) % MOD
                            else:  # 移出边界
                                result = (result + dp[k][i][j]) % MOD
        return result
