class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.max_gold = 0
        
        # 深度优先搜索函数
        def dfs(i, j, current_gold):
            # 保存当前单元格的值
            temp = grid[i][j]
            # 更新当前收集的黄金数量
            current_gold += temp
            # 更新最大黄金数量
            self.max_gold = max(self.max_gold, current_gold)
            # 标记当前单元格为已访问
            grid[i][j] = 0
            
            # 四个方向的移动：上、右、下、左
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # 检查新位置是否在网格范围内且包含黄金
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0:
                    dfs(ni, nj, current_gold)
            
            # 回溯，恢复单元格的原始值
            grid[i][j] = temp
        
        # 遍历网格中的每个单元格
        for i in range(m):
            for j in range(n):
                # 如果当前单元格有黄金，则从该位置开始DFS
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        
        return self.max_gold
