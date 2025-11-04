"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 如果根节点为空，直接返回空列表
        if not root:
            return []
        
        # 初始化结果列表和队列
        result = []
        queue = deque([root])
        
        # 当队列不为空时继续循环
        while queue:
            # 当前层的节点值列表
            level = []
            # 当前层的节点数量
            level_size = len(queue)
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                # 从队列左侧取出节点
                node = queue.popleft()
                # 将节点值添加到当前层列表
                level.append(node.val)
                
                # 如果节点有子节点，将所有子节点加入队列
                if node.children:
                    for child in node.children:
                        queue.append(child)
            
            # 将当前层的结果添加到最终结果中
            result.append(level)
        
        return result
