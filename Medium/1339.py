MOD = 10**9 + 7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 计算整棵树的总和
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
        
        total_sum = get_total_sum(root)
        self.max_product = 0
        
        # 后序遍历计算每个子树的和，并更新最大乘积
        def dfs(node):
            if not node:
                return 0
            # 计算当前子树的和
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            current_sum = node.val + left_sum + right_sum
            
            # 计算删除当前节点与父节点之间的边后的乘积
            product = current_sum * (total_sum - current_sum)
            if product > self.max_product:
                self.max_product = product
                
            return current_sum
        
        dfs(root)
        return self.max_product % MOD
