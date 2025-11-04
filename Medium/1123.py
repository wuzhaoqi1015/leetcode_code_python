# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 定义DFS函数，返回当前节点的深度和包含所有最深叶节点的最近公共祖先
        def dfs(node):
            if not node:
                return 0, None
            # 递归处理左右子树
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            # 如果左右子树深度相同，当前节点就是最近公共祖先
            if left_depth == right_depth:
                return left_depth + 1, node
            # 如果左子树更深，返回左子树的结果
            elif left_depth > right_depth:
                return left_depth + 1, left_lca
            # 如果右子树更深，返回右子树的结果
            else:
                return right_depth + 1, right_lca
        
        # 从根节点开始DFS遍历
        depth, lca_node = dfs(root)
        return lca_node
