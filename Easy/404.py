# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 如果根节点为空，直接返回0
        if not root:
            return 0
            
        total = 0
        
        # 检查左子节点是否存在
        if root.left:
            # 如果左子节点是叶子节点（没有左右子节点）
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                # 递归处理左子树
                total += self.sumOfLeftLeaves(root.left)
        
        # 递归处理右子树
        total += self.sumOfLeftLeaves(root.right)
        
        return total
