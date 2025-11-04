# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 使用中序遍历，二叉搜索树的中序遍历是升序序列
        stack = []
        curr = root
        count = 0
        
        while stack or curr:
            # 遍历到最左节点
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 弹出栈顶节点
            curr = stack.pop()
            count += 1
            
            # 如果当前是第k个节点，返回其值
            if count == k:
                return curr.val
            
            # 转向右子树
            curr = curr.right
