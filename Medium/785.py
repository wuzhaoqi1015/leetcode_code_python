from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}  # 记录每个节点的颜色，0和1表示两种颜色
        
        for node in range(n):
            if node not in color:  # 如果节点未被染色
                stack = [node]
                color[node] = 0  # 起始节点染为0
                
                while stack:
                    current = stack.pop()
                    for neighbor in graph[current]:
                        if neighbor not in color:  # 如果邻居节点未被染色
                            color[neighbor] = color[current] ^ 1  # 染为相反颜色
                            stack.append(neighbor)
                        elif color[neighbor] == color[current]:  # 如果颜色冲突
                            return False
        return True
