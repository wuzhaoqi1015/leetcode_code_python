# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 使用字典记录每个节点的深度和父节点值
        node_info = {}
        
        # DFS遍历二叉树，记录每个节点的深度和父节点
        def dfs(node, depth, parent):
            if not node:
                return
            # 记录当前节点的深度和父节点
            node_info[node.val] = (depth, parent)
            # 递归遍历左右子树
            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)
        
        # 从根节点开始遍历，根节点的父节点设为None
        dfs(root, 0, None)
        
        # 检查x和y对应的节点信息是否存在
        if x not in node_info or y not in node_info:
            return False
        
        # 获取x和y的深度和父节点
        depth_x, parent_x = node_info[x]
        depth_y, parent_y = node_info[y]
        
        # 堂兄弟节点条件：深度相同但父节点不同
        return depth_x == depth_y and parent_x != parent_y
