# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0  # 存储最长路径长度
        
        def dfs(node):
            if not node:
                return 0
                
            left_length = dfs(node.left)  # 左子树的最长同值路径长度
            right_length = dfs(node.right)  # 右子树的最长同值路径长度
            
            # 计算当前节点与左子节点的同值路径长度
            left_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
                
            # 计算当前节点与右子节点的同值路径长度
            right_arrow = 0
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
                
            # 更新全局最长路径：当前节点作为连接点的路径长度
            self.max_length = max(self.max_length, left_arrow + right_arrow)
            
            # 返回以当前节点为端点的最长同值路径长度
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return self.max_length
