"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from typing import Optional, List
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 如果根节点为空，深度为0
        if not root:
            return 0
        
        # 使用队列进行BFS遍历
        queue = deque([root])
        depth = 0
        
        while queue:
            # 当前层的节点数
            level_size = len(queue)
            # 处理当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                # 将当前节点的所有子节点加入队列
                if node.children:
                    for child in node.children:
                        queue.append(child)
            # 完成一层遍历，深度加1
            depth += 1
        
        return depth
