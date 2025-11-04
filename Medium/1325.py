# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # 使用后序遍历递归删除目标叶子节点
        def dfs(node):
            if not node:
                return None
            # 递归处理左子树
            node.left = dfs(node.left)
            # 递归处理右子树
            node.right = dfs(node.right)
            # 如果当前节点是叶子节点且值等于target，则删除该节点
            if not node.left and not node.right and node.val == target:
                return None
            return node
        
        return dfs(root)
