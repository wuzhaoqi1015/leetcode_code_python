# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 使用逆中序遍历（右-根-左）来累加节点值
        self.total = 0
        
        def dfs(node):
            if not node:
                return
            # 先遍历右子树
            dfs(node.right)
            # 更新当前节点值
            self.total += node.val
            node.val = self.total
            # 再遍历左子树
            dfs(node.left)
        
        dfs(root)
        return root
