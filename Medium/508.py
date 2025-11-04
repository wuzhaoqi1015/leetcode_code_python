from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # 使用字典记录每个子树和出现的频率
        sum_freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            # 计算当前节点的子树和
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = node.val + left_sum + right_sum
            # 更新频率计数
            sum_freq[total_sum] += 1
            return total_sum
        
        # 从根节点开始深度优先遍历
        dfs(root)
        
        # 找出最大频率
        max_freq = max(sum_freq.values()) if sum_freq else 0
        
        # 收集所有出现次数等于最大频率的子树和
        result = [s for s, freq in sum_freq.items() if freq == max_freq]
        
        return result
