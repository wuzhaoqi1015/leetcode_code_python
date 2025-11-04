# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如果根节点为空或者新值大于根节点值，则新节点成为根节点
        if not root or val > root.val:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        # 否则递归地在右子树中插入
        # 因为新值要添加到数组末尾，所以应该插入到右子树路径上
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
