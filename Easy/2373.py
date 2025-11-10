class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # 创建结果矩阵，大小为(n-2) x (n-2)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        
        # 遍历每个3x3窗口的左上角位置
        for i in range(n - 2):
            for j in range(n - 2):
                # 在当前3x3窗口内寻找最大值
                max_val = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if grid[x][y] > max_val:
                            max_val = grid[x][y]
                maxLocal[i][j] = max_val
                
        return maxLocal
