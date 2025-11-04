# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        from collections import deque
        
        queue = deque([root])  # 初始化队列，包含根节点
        max_sum = float('-inf')  # 记录最大层和
        min_level = 0  # 记录最小层号
        current_level = 1  # 当前层号从1开始
        
        while queue:
            level_size = len(queue)  # 当前层的节点数
            level_sum = 0  # 当前层的节点值之和
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # 将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 更新最大层和及最小层号
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = current_level
            
            current_level += 1  # 进入下一层
        
        return min_level
