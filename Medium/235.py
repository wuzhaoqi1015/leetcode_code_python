# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 利用二叉搜索树的性质：左子树所有节点值小于根节点，右子树所有节点值大于根节点
        current = root
        while current:
            # 如果p和q的值都小于当前节点值，说明最近公共祖先在左子树
            if p.val < current.val and q.val < current.val:
                current = current.left
            # 如果p和q的值都大于当前节点值，说明最近公共祖先在右子树
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # 否则当前节点就是最近公共祖先
            # 情况包括：p和q分别在当前节点两侧，或者当前节点就是p或q之一
            else:
                return current
