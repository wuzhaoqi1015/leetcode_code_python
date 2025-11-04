class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] 表示以(i,j)为右下角的最大正方形边长
        dp = [[0] * n for _ in range(m)]
        total = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # 第一行或第一列，最大边长只能是1
                        dp[i][j] = 1
                    else:
                        # 状态转移：取左、上、左上三个位置的最小值加1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 以(i,j)为右下角的正方形个数等于最大边长
                    total += dp[i][j]
                else:
                    dp[i][j] = 0
                    
        return total
