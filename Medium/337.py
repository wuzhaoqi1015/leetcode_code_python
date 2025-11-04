# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 使用后序遍历，返回一个元组 (不偷当前节点的最大值, 偷当前节点的最大值)
        def dfs(node):
            if not node:
                return (0, 0)
            
            # 递归处理左右子树
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 不偷当前节点：左右子树可以偷或不偷的最大值之和
            not_rob = max(left) + max(right)
            
            # 偷当前节点：当前节点值 + 不偷左右子节点的值
            rob = node.val + left[0] + right[0]
            
            return (not_rob, rob)
        
        result = dfs(root)
        return max(result)
