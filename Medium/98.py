# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 使用中序遍历验证二叉搜索树
        # 初始化前一个节点值为负无穷
        self.prev = float('-inf')
        
        def inorder_traversal(node):
            if not node:
                return True
            # 遍历左子树
            if not inorder_traversal(node.left):
                return False
            # 检查当前节点值是否大于前一个节点值
            if node.val <= self.prev:
                return False
            # 更新前一个节点值为当前节点值
            self.prev = node.val
            # 遍历右子树
            return inorder_traversal(node.right)
        
        return inorder_traversal(root)
