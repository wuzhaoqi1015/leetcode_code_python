class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])
        max_area = 0
        
        # 深度优先搜索函数
        def dfs(i, j):
            # 如果越界或者当前单元格不是土地，返回0
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            # 将当前土地标记为已访问（沉没岛屿）
            grid[i][j] = 0
            
            # 初始化面积为1（当前单元格）
            area = 1
            
            # 向四个方向递归搜索相邻土地
            area += dfs(i + 1, j)  # 向下
            area += dfs(i - 1, j)  # 向上
            area += dfs(i, j + 1)  # 向右
            area += dfs(i, j - 1)  # 向左
            
            return area
        
        # 遍历整个网格
        for i in range(m):
            for j in range(n):
                # 如果发现土地，进行深度优先搜索计算岛屿面积
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    # 更新最大岛屿面积
                    max_area = max(max_area, current_area)
        
        return max_area
