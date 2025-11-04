from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        if original_color == color:
            return grid
        
        visited = [[False] * n for _ in range(m)]
        borders = []
        
        # DFS遍历连通分量
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != original_color or visited[r][c]:
                return
            visited[r][c] = True
            
            # 检查当前点是否为边界
            is_border = False
            # 检查四个方向
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # 如果相邻点超出边界或者颜色不同，则是边界
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != original_color:
                    is_border = True
                    break
            
            if is_border:
                borders.append((r, c))
            
            # 继续遍历四个方向
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)
        
        # 从起始点开始DFS
        dfs(row, col)
        
        # 为边界点着色
        for r, c in borders:
            grid[r][c] = color
        
        return grid
