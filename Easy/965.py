# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 获取根节点的值作为基准值
        base_val = root.val
        
        # 使用深度优先搜索遍历二叉树
        def dfs(node):
            # 如果节点为空，返回True
            if not node:
                return True
            # 如果当前节点值与基准值不同，返回False
            if node.val != base_val:
                return False
            # 递归检查左右子树
            return dfs(node.left) and dfs(node.right)
        
        # 从根节点开始遍历
        return dfs(root)
