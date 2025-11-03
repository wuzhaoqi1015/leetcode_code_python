# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        left_to_right = True  # 标记当前层的遍历方向
        
        while queue:
            level_size = len(queue)
            current_level = collections.deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # 根据方向决定添加到队列的哪一端
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                
                # 将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(current_level))
            left_to_right = not left_to_right  # 切换方向
        
        return result
