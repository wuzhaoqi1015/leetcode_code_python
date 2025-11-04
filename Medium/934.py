from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 找到第一个岛屿的所有位置
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2  # 标记为已访问
            queue.append((i, j, 0))  # 将边界点加入队列，距离初始为0
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        queue = deque()
        found = False
        # 寻找第一个岛屿
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # BFS扩展第一个岛屿，寻找最短路径到第二个岛屿
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:  # 找到第二个岛屿
                        return dist
                    elif grid[nx][ny] == 0:  # 水域，继续扩展
                        grid[nx][ny] = 2  # 标记为已访问
                        queue.append((nx, ny, dist + 1))
        return -1
