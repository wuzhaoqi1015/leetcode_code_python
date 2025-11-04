from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # 初始化队列和新鲜橘子计数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # 记录位置和时间
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # 如果没有新鲜橘子，直接返回0
        if fresh_count == 0:
            return 0
        
        # 四个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # BFS遍历
        while queue:
            i, j, time = queue.popleft()
            minutes = max(minutes, time)
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    queue.append((ni, nj, time + 1))
        
        # 检查是否还有新鲜橘子
        return minutes if fresh_count == 0 else -1
