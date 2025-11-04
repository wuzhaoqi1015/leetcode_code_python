class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 创建两个DP数组，分别记录从当前位置向左和向上连续1的个数
        left = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        
        # 初始化DP数组
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 计算向左连续1的个数
                    left[i][j] = 1 if j == 0 else left[i][j-1] + 1
                    # 计算向上连续1的个数
                    up[i][j] = 1 if i == 0 else up[i-1][j] + 1
        
        max_side = 0
        # 遍历每个点作为正方形的右下角
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 当前可能的最大边长
                    current_side = min(left[i][j], up[i][j])
                    # 检查是否能形成正方形
                    for k in range(current_side, 0, -1):
                        # 检查左上角的点是否满足条件
                        if min(up[i][j-k+1], left[i-k+1][j]) >= k:
                            max_side = max(max_side, k)
                            break
        
        return max_side * max_side
