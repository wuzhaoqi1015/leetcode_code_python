# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = collections.deque()
        queue.append((root, 0))  # 存储节点和对应的位置索引
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]  # 当前层第一个节点的索引
            _, last_index = queue[-1]  # 当前层最后一个节点的索引
            max_width = max(max_width, last_index - first_index + 1)
            
            for i in range(level_length):
                node, index = queue.popleft()
                # 计算子节点的位置索引，避免索引溢出
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width
