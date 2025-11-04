# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 处理depth为1的特殊情况
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # 使用BFS遍历到depth-1层
        from collections import deque
        queue = deque([root])
        current_depth = 1
        
        while queue:
            level_size = len(queue)
            # 如果到达目标深度的上一层
            if current_depth == depth - 1:
                for _ in range(level_size):
                    node = queue.popleft()
                    # 创建新的左右子节点
                    new_left = TreeNode(val)
                    new_right = TreeNode(val)
                    # 将原左子树连接到新左节点的左子树
                    new_left.left = node.left
                    # 将原右子树连接到新右节点的右子树
                    new_right.right = node.right
                    # 更新当前节点的左右子节点
                    node.left = new_left
                    node.right = new_right
                break
            else:
                # 继续遍历下一层
                for _ in range(level_size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                current_depth += 1
        
        return root
