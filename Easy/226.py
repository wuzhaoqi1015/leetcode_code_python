# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果根节点为空，直接返回
        if not root:
            return None
        
        # 递归翻转左子树
        left_inverted = self.invertTree(root.left)
        # 递归翻转右子树
        right_inverted = self.invertTree(root.right)
        
        # 交换左右子树
        root.left = right_inverted
        root.right = left_inverted
        
        # 返回翻转后的根节点
        return root
