# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(node, parent, grandparent):
            if not node:
                return
            
            # 如果祖父节点存在且值为偶数，累加当前节点值
            if grandparent and grandparent.val % 2 == 0:
                self.total += node.val
            
            # 递归遍历左右子树，当前节点作为父节点，原父节点作为祖父节点
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        
        # 从根节点开始遍历，初始父节点和祖父节点都为None
        dfs(root, None, None)
        return self.total
