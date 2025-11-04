# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 中序遍历获取有序节点值列表
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # 根据有序列表构建平衡二叉搜索树
        def build_balanced_bst(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = build_balanced_bst(values[:mid])
            root.right = build_balanced_bst(values[mid+1:])
            return root
        
        # 获取有序节点值
        sorted_values = inorder_traversal(root)
        # 构建并返回平衡后的二叉搜索树
        return build_balanced_bst(sorted_values)
