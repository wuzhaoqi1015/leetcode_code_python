# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 使用迭代方法进行前序遍历
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            
            if prev:
                prev.left = None
                prev.right = curr
            
            # 先将右子树入栈，再将左子树入栈
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
            prev = curr
