# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)  # 初始化时将所有左节点压入栈

    def _leftmost_inorder(self, node):
        # 将给定节点的所有左子节点压入栈
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # 弹出栈顶节点，这是当前最小的节点
        top_node = self.stack.pop()
        
        # 如果弹出的节点有右子树，处理右子树的所有左节点
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        
        return top_node.val

    def hasNext(self) -> bool:
        # 如果栈不为空，说明还有节点需要遍历
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
