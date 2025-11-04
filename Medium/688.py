class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # 定义骑士的8个移动方向
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        # 初始化动态规划数组，dp[i][j]表示在某个位置的概率
        # 使用三维数组dp[step][i][j]表示移动step步后停留在(i,j)的概率
        # 由于k可能为0，需要特殊处理
        if k == 0:
            return 1.0
            
        # 初始化dp数组，使用两个二维数组交替更新
        dp_prev = [[0.0] * n for _ in range(n)]
        dp_prev[row][column] = 1.0
        
        for step in range(1, k + 1):
            dp_curr = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp_prev[i][j] > 0:
                        for dx, dy in directions:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < n and 0 <= nj < n:
                                dp_curr[ni][nj] += dp_prev[i][j] / 8.0
            dp_prev = dp_curr
        
        # 计算总概率
        total_prob = 0.0
        for i in range(n):
            for j in range(n):
                total_prob += dp_prev[i][j]
                
        return total_prob
