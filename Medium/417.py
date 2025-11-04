class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        # 创建两个访问矩阵，分别记录能到达太平洋和大西洋的位置
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        # 定义DFS函数
        def dfs(r, c, reachable):
            # 标记当前位置为可达
            reachable[r][c] = True
            # 四个方向：上、右、下、左
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 检查新位置是否在矩阵范围内
                if 0 <= nr < m and 0 <= nc < n:
                    # 检查新位置是否未被访问且高度不低于当前位置
                    if not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)
        
        # 从太平洋边界开始DFS（左边界和上边界）
        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)
        
        # 从大西洋边界开始DFS（右边界和下边界）
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)
        
        # 收集既能到达太平洋又能到达大西洋的位置
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result
