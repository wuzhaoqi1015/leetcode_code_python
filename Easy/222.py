# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 计算左右子树的高度
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        
        # 如果左右子树高度相等，说明左子树是满二叉树
        if left_height == right_height:
            # 左子树节点数：2^left_height - 1，加上根节点，再加上右子树节点数
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # 右子树是满二叉树，高度比左子树少1
            return (1 << right_height) + self.countNodes(root.left)
    
    def _get_height(self, node):
        # 计算完全二叉树的高度（沿着左子树走）
        height = 0
        while node:
            height += 1
            node = node.left
        return height
