# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 使用深度优先搜索遍历二叉搜索树
        def dfs(node):
            if not node:
                return 0
            total = 0
            # 如果当前节点值在范围内，累加
            if low <= node.val <= high:
                total += node.val
            # 如果当前节点值大于low，需要搜索左子树
            if node.val > low:
                total += dfs(node.left)
            # 如果当前节点值小于high，需要搜索右子树
            if node.val < high:
                total += dfs(node.right)
            return total
        
        return dfs(root)
