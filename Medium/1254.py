class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # 深度优先搜索函数
        def dfs(i, j):
            # 如果到达边界，说明不是封闭岛屿
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            # 如果是水域或已访问过，返回True
            if grid[i][j] == 1:
                return True
                
            # 标记为已访问
            grid[i][j] = 1
            
            # 递归访问四个方向
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            
            # 只有四个方向都是封闭的，当前岛屿才是封闭的
            return up and down and left and right
        
        count = 0
        # 遍历整个网格
        for i in range(m):
            for j in range(n):
                # 找到陆地且未被访问过
                if grid[i][j] == 0:
                    # 如果DFS返回True，说明是封闭岛屿
                    if dfs(i, j):
                        count += 1
                        
        return count
