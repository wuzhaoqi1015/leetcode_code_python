# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 更新直径：当前节点的左右子树深度之和
            self.diameter = max(self.diameter, left_depth + right_depth)
            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
