# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node, is_left, length):
            if not node:
                return
            self.max_length = max(self.max_length, length)
            if is_left:
                dfs(node.left, False, length + 1)  # 继续左方向
                dfs(node.right, True, 1)  # 改变方向重新开始
            else:
                dfs(node.right, True, length + 1)  # 继续右方向
                dfs(node.left, False, 1)  # 改变方向重新开始
        
        if root:
            dfs(root.left, False, 1)  # 从根节点向左开始
            dfs(root.right, True, 1)  # 从根节点向右开始
        
        return self.max_length
