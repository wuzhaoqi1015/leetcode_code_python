class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])
        
        # 定义深度优先搜索函数
        def dfs(i, j):
            # 如果当前位置超出边界或者是海洋，直接返回
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            # 将当前陆地标记为海洋（已访问）
            grid[i][j] = 0
            # 向四个方向进行深度优先搜索
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # 遍历网格的四条边界
        # 遍历第一行和最后一行
        for i in [0, m - 1]:
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
        
        # 遍历第一列和最后一列（跳过四个角，避免重复）
        for i in range(1, m - 1):
            for j in [0, n - 1]:
                if grid[i][j] == 1:
                    dfs(i, j)
        
        # 统计剩余的陆地数量（即无法到达边界的陆地）
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        
        return count
