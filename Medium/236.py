# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果当前节点为空，或者当前节点就是p或q，直接返回当前节点
        if not root or root == p or root == q:
            return root
        
        # 递归在左子树中查找p和q
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归在右子树中查找p和q
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左右子树都找到了节点，说明当前节点就是最近公共祖先
        if left and right:
            return root
        
        # 如果只有左子树找到了节点，返回左子树的结果
        if left:
            return left
        
        # 如果只有右子树找到了节点，返回右子树的结果
        return right
