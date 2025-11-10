# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []
        
        def inorder_traversal(node):
            if not node:
                return
            
            inorder_traversal(node.left)
            
            # 处理当前节点值
            if node.val == self.current_val:
                self.current_count += 1
            else:
                self.current_val = node.val
                self.current_count = 1
            
            # 更新众数列表
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [self.current_val]
            elif self.current_count == self.max_count:
                self.modes.append(self.current_val)
            
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.modes
