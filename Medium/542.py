from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # 初始化结果矩阵，所有位置设为-1表示未访问
        dist = [[-1] * n for _ in range(m)]
        # 使用队列进行BFS
        queue = deque()
        # 将所有0的位置加入队列，并设置距离为0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        # 定义四个方向的移动
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # BFS遍历
        while queue:
            x, y = queue.popleft()
            # 遍历四个方向
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 检查新位置是否在矩阵范围内且未访问过
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    # 更新距离
                    dist[nx][ny] = dist[x][y] + 1
                    # 将新位置加入队列
                    queue.append((nx, ny))
        return dist
