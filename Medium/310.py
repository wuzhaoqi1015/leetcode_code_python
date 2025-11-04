from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 处理特殊情况：只有一个节点
        if n == 1:
            return [0]
        
        # 构建邻接表
        graph = [[] for _ in range(n)]
        degree = [0] * n  # 记录每个节点的度数
        
        # 填充邻接表和度数数组
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # 初始化队列，将所有度数为1的叶子节点加入
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        remaining_nodes = n
        # 当剩余节点数大于2时继续处理
        while remaining_nodes > 2:
            # 当前层的节点数量
            level_size = len(queue)
            remaining_nodes -= level_size
            
            # 处理当前层的所有叶子节点
            for _ in range(level_size):
                leaf = queue.popleft()
                
                # 遍历叶子节点的邻居
                for neighbor in graph[leaf]:
                    # 减少邻居的度数
                    degree[neighbor] -= 1
                    # 如果邻居成为新的叶子节点，加入队列
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        # 返回队列中剩余的节点，这些就是最小高度树的根节点
        return list(queue)
