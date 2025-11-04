# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 查找要删除的节点
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 找到要删除的节点
            # 情况1：没有左子树
            if not root.left:
                return root.right
            # 情况2：没有右子树
            elif not root.right:
                return root.left
            # 情况3：有两个子节点
            else:
                # 找到右子树的最小节点
                min_node = self._find_min(root.right)
                # 用最小节点的值替换当前节点的值
                root.val = min_node.val
                # 删除右子树中的最小节点
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        # 在BST中找到最小节点（最左节点）
        while node.left:
            node = node.left
        return node
