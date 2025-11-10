class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        # 遍历每个格子
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # 如果是陆地
                    # 检查上方边界或上方是否为水域
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # 检查下方边界或下方是否为水域
                    if i == rows-1 or grid[i+1][j] == 0:
                        perimeter += 1
                    # 检查左方边界或左方是否为水域
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # 检查右方边界或右方是否为水域
                    if j == cols-1 or grid[i][j+1] == 0:
                        perimeter += 1
        
        return perimeter
