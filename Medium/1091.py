class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 如果起点或终点是障碍物，直接返回-1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # 8个方向的移动向量
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # 使用BFS队列，存储(x,y,步数)
        from collections import deque
        queue = deque()
        queue.append((0, 0, 1))  # 起点，步数为1
        
        # 标记已访问的节点
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while queue:
            x, y, steps = queue.popleft()
            
            # 到达终点
            if x == n-1 and y == n-1:
                return steps
            
            # 遍历8个方向
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 检查新位置是否在网格范围内且未被访问过且是畅通的
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))
        
        # 如果队列为空仍未到达终点，返回-1
        return -1
