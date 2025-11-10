# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder_traversal(node):
            if not node:
                return
            
            # 遍历左子树
            inorder_traversal(node.left)
            
            # 处理当前节点
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            
            self.prev = node.val
            
            # 遍历右子树
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.min_diff
