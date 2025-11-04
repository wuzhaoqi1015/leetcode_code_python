from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构建图结构，使用邻接表存储变量之间的关系和权重
        graph = defaultdict(dict)
        
        # 填充图数据，建立双向关系
        for (a, b), value in zip(equations, values):
            graph[a][b] = value      # a/b = value
            graph[b][a] = 1.0 / value  # b/a = 1/value
        
        result = []
        
        # 处理每个查询
        for c, d in queries:
            # 如果查询中的变量不在图中，直接返回-1.0
            if c not in graph or d not in graph:
                result.append(-1.0)
                continue
            
            # 如果查询的两个变量相同，返回1.0
            if c == d:
                result.append(1.0)
                continue
            
            # 使用BFS查找路径并计算结果
            visited = set()
            queue = deque()
            queue.append((c, 1.0))  # (当前节点, 累积乘积)
            visited.add(c)
            found = False
            
            while queue and not found:
                node, current_value = queue.popleft()
                
                # 遍历当前节点的所有邻居
                for neighbor, weight in graph[node].items():
                    if neighbor == d:
                        # 找到目标节点，计算最终结果
                        result.append(current_value * weight)
                        found = True
                        break
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_value * weight))
            
            # 如果没有找到路径，返回-1.0
            if not found:
                result.append(-1.0)
        
        return result
