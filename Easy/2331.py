# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 如果是叶子节点，直接返回对应的布尔值
        if root.left is None and root.right is None:
            return root.val == 1
        
        # 递归计算左子树的值
        left_val = self.evaluateTree(root.left)
        # 递归计算右子树的值
        right_val = self.evaluateTree(root.right)
        
        # 根据当前节点的运算符进行逻辑运算
        if root.val == 2:  # OR 运算
            return left_val or right_val
        elif root.val == 3:  # AND 运算
            return left_val and right_val
