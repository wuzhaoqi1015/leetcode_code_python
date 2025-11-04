from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 构建邻接表
        graph = [[] for _ in range(n+1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # 颜色数组，0表示未染色，1和-1表示两种颜色
        color = [0] * (n+1)
        
        # BFS遍历所有节点
        for i in range(1, n+1):
            if color[i] == 0:  # 未染色的节点
                queue = deque([i])
                color[i] = 1  # 初始染色为1
                
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == 0:  # 邻居未染色
                            color[neighbor] = -color[node]  # 染相反颜色
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:  # 颜色冲突
                            return False
        return True
