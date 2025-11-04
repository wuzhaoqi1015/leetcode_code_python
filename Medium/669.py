# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 如果根节点为空，直接返回None
        if not root:
            return None
        
        # 如果当前节点值小于low，说明当前节点及其左子树都不在范围内
        # 只需要处理右子树
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # 如果当前节点值大于high，说明当前节点及其右子树都不在范围内
        # 只需要处理左子树
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # 当前节点在范围内，递归修剪左右子树
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
