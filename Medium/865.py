# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 定义辅助函数，返回当前节点的深度和包含所有最深节点的子树根节点
        def dfs(node):
            if not node:
                return 0, None  # 空节点深度为0，子树为None
            left_depth, left_subtree = dfs(node.left)  # 递归处理左子树
            right_depth, right_subtree = dfs(node.right)  # 递归处理右子树
            # 如果左右子树深度相同，当前节点就是包含所有最深节点的最小子树
            if left_depth == right_depth:
                return left_depth + 1, node
            # 如果左子树更深，返回左子树的结果
            elif left_depth > right_depth:
                return left_depth + 1, left_subtree
            # 如果右子树更深，返回右子树的结果
            else:
                return right_depth + 1, right_subtree
        
        # 从根节点开始深度优先搜索
        _, result = dfs(root)
        return result
