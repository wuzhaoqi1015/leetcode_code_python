from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 初始化队列和距离矩阵
        queue = deque()
        dist = [[-1] * n for _ in range(n)]
        
        # 将所有陆地单元格加入队列，并设置距离为0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    dist[i][j] = 0
        
        # 如果没有陆地或全是陆地，返回-1
        if not queue or len(queue) == n * n:
            return -1
        
        # 定义四个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_distance = -1
        
        # BFS遍历
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 检查新坐标是否在网格范围内且未被访问过
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    max_distance = max(max_distance, dist[nx][ny])
                    queue.append((nx, ny))
        
        return max_distance
