# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果根节点为空，直接返回空列表
        if not root:
            return []
        
        # 初始化结果列表和队列
        result = []
        queue = collections.deque([root])
        
        # 使用BFS进行层序遍历
        while queue:
            level_size = len(queue)
            current_level = []
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 将左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 将当前层的结果添加到结果列表
            result.append(current_level)
        
        # 反转结果列表，实现自底向上的层序遍历
        return result[::-1]
