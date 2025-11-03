# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # 使用字典存储原节点到克隆节点的映射
        visited = {}
        
        def dfs(original_node):
            # 如果节点已经访问过，直接返回克隆节点
            if original_node in visited:
                return visited[original_node]
            
            # 创建当前节点的克隆
            clone_node = Node(original_node.val)
            visited[original_node] = clone_node
            
            # 递归克隆所有邻居节点
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)
