# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = str(root.val)
        
        # 处理左子树
        if root.left or root.right:
            # 左子树必须表示，即使为空也要用空括号
            left_str = self.tree2str(root.left)
            result += "(" + left_str + ")"
        
        # 处理右子树
        if root.right:
            # 只有当右子树存在时才需要表示右子树
            right_str = self.tree2str(root.right)
            result += "(" + right_str + ")"
        
        return result
