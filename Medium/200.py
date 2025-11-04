class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            # 检查边界条件和当前单元格是否为陆地
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            # 将访问过的陆地标记为'0'（水）
            grid[i][j] = '0'
            # 递归访问四个方向的相邻单元格
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                # 当发现陆地时，进行深度优先搜索并增加岛屿计数
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
