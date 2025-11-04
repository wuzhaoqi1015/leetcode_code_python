# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            # 计算左右子树需要传递的硬币数量
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            # 当前节点的硬币流动量（需要移动的次数）
            self.moves += abs(left_excess) + abs(right_excess)
            # 返回当前节点的硬币净流出量
            return node.val + left_excess + right_excess - 1
        
        dfs(root)
        return self.moves
