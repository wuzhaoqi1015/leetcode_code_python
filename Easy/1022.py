# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            # 更新当前路径的值，左移一位并加上当前节点的值
            current_sum = (current_sum << 1) | node.val
            # 如果是叶子节点，返回当前路径的值
            if not node.left and not node.right:
                return current_sum
            # 递归计算左右子树的和
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)
