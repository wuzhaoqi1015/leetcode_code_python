# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 定义递归函数，返回当前子树是否包含1
        def contains_one(node):
            if not node:
                return False
            
            # 递归检查左右子树
            left_contains = contains_one(node.left)
            right_contains = contains_one(node.right)
            
            # 如果左子树不包含1，则剪枝
            if not left_contains:
                node.left = None
            # 如果右子树不包含1，则剪枝
            if not right_contains:
                node.right = None
            
            # 返回当前子树是否包含1（当前节点值为1或左右子树包含1）
            return node.val == 1 or left_contains or right_contains
        
        # 如果整棵树都不包含1，返回None，否则返回修剪后的树
        return root if contains_one(root) else None
