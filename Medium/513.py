# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        # 使用BFS层序遍历，记录每层第一个节点的值
        queue = deque([root])
        result = root.val
        
        while queue:
            level_size = len(queue)
            # 记录当前层的第一个节点值
            result = queue[0].val
            
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = queue.popleft()
                
                # 将左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # 返回最后一层的第一个节点值
        return result
