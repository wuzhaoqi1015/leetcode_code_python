# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # 定义全局变量记录左子树、右子树和父节点方向的数量
        left_count = 0
        right_count = 0
        
        def count_nodes(node):
            if not node:
                return 0
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            # 如果当前节点是x节点，记录其左右子树的节点数
            if node.val == x:
                nonlocal left_count, right_count
                left_count = left
                right_count = right
            return left + right + 1
        
        count_nodes(root)
        # 计算父节点方向的节点数
        parent_count = n - left_count - right_count - 1
        # 二号玩家可以选择三个方向中最大的那个
        max_region = max(left_count, right_count, parent_count)
        # 如果最大区域超过总节点数的一半，二号玩家可以获胜
        return max_region > n // 2
