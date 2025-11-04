from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 构建邻接表，0表示红色边，1表示蓝色边
        graph = [[[] for _ in range(n)] for _ in range(2)]
        
        # 填充红色边
        for u, v in redEdges:
            graph[0][u].append(v)
        
        # 填充蓝色边
        for u, v in blueEdges:
            graph[1][u].append(v)
        
        # 初始化距离数组，-1表示不可达
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = 0  # 从红色边开始到节点0的距离
        dist[1][0] = 0  # 从蓝色边开始到节点0的距离
        
        # 使用BFS队列，每个元素为(节点, 颜色, 距离)
        # 颜色0表示下一步需要蓝色边，1表示下一步需要红色边
        queue = deque()
        queue.append((0, 0, 0))  # (节点, 下一步需要的颜色, 距离)
        queue.append((0, 1, 0))  # (节点, 下一步需要的颜色, 距离)
        
        while queue:
            node, next_color, steps = queue.popleft()
            
            # 遍历所有可能的下一跳
            for neighbor in graph[next_color][node]:
                # 如果该节点在该颜色下还未被访问过
                if dist[next_color][neighbor] == -1:
                    dist[next_color][neighbor] = steps + 1
                    # 切换颜色，0变1，1变0
                    queue.append((neighbor, 1 - next_color, steps + 1))
        
        # 构建最终答案，取两种颜色路径中的最小值
        answer = []
        for i in range(n):
            if dist[0][i] == -1 and dist[1][i] == -1:
                answer.append(-1)
            elif dist[0][i] == -1:
                answer.append(dist[1][i])
            elif dist[1][i] == -1:
                answer.append(dist[0][i])
            else:
                answer.append(min(dist[0][i], dist[1][i]))
        
        return answer
