# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # 定义DFS函数，返回当前节点是否应该保留
        def dfs(node, current_sum):
            # 如果节点为空，直接返回False
            if not node:
                return False
            
            # 计算当前路径和
            current_sum += node.val
            
            # 如果是叶子节点，检查路径和是否满足条件
            if not node.left and not node.right:
                return current_sum >= limit
            
            # 递归检查左右子树
            left_valid = dfs(node.left, current_sum)
            right_valid = dfs(node.right, current_sum)
            
            # 根据子树结果更新左右子节点
            if not left_valid:
                node.left = None
            if not right_valid:
                node.right = None
            
            # 如果左右子树至少有一个有效，则当前节点有效
            return left_valid or right_valid
        
        # 从根节点开始DFS，初始和为0
        root_valid = dfs(root, 0)
        
        # 如果根节点无效，返回None，否则返回处理后的根节点
        return root if root_valid else None
