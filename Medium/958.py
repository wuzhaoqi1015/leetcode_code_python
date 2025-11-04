# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        from collections import deque
        queue = deque([root])
        found_null = False  # 标记是否已经遇到空节点
        
        while queue:
            node = queue.popleft()
            
            # 如果遇到空节点，标记为True
            if not node:
                found_null = True
                continue
            
            # 如果之前已经遇到空节点，但当前节点不为空，说明不是完全二叉树
            if found_null:
                return False
            
            # 将左右子节点加入队列（即使为空也要加入）
            queue.append(node.left)
            queue.append(node.right)
        
        return True
