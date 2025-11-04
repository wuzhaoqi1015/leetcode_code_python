# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 如果两个节点都为空，则等价
        if not root1 and not root2:
            return True
        # 如果只有一个节点为空，或者节点值不相等，则不等价
        if not root1 or not root2 or root1.val != root2.val:
            return False
        # 递归检查两种情况：不翻转和翻转
        # 不翻转：左右子树分别对应相等
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # 翻转：左子树与右子树交换后对应相等
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        # 只要有一种情况满足即可
        return no_flip or flip
