# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def dfs(node, min_val, max_val):
            if not node:
                return
            
            # 更新当前路径上的最小值和最大值
            current_min = min(min_val, node.val)
            current_max = max(max_val, node.val)
            
            # 计算当前节点与路径上最小值和最大值的差值
            self.result = max(self.result, abs(node.val - min_val), abs(node.val - max_val))
            
            # 递归遍历左右子树
            dfs(node.left, current_min, current_max)
            dfs(node.right, current_min, current_max)
        
        # 从根节点开始遍历，初始最小值和最大值都设为根节点的值
        dfs(root, root.val, root.val)
        return self.result
