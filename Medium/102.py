# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果根节点为空，直接返回空列表
        if not root:
            return []
        
        # 初始化结果列表和队列
        result = []
        queue = collections.deque()
        queue.append(root)
        
        # 使用BFS进行层序遍历
        while queue:
            level_size = len(queue)  # 当前层的节点数量
            current_level = []  # 存储当前层的节点值
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()  # 从队列左侧取出节点
                current_level.append(node.val)  # 将节点值加入当前层列表
                
                # 如果存在左子节点，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果存在右子节点，加入队列
                if node.right:
                    queue.append(node.right)
            
            # 将当前层的结果加入最终结果
            result.append(current_level)
        
        return result
