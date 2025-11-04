# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        
        # 使用前缀和思想，记录从根节点到当前节点的路径和出现次数
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # 空路径的和为0
        
        def dfs(node, current_sum):
            if not node:
                return 0
                
            current_sum += node.val
            # 查找是否存在前缀和等于 current_sum - targetSum
            count = prefix_sum_count[current_sum - targetSum]
            
            # 更新当前前缀和的出现次数
            prefix_sum_count[current_sum] += 1
            
            # 递归遍历左右子树
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # 回溯，恢复状态
            prefix_sum_count[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)
