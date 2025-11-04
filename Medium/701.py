# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如果根节点为空，直接创建新节点作为根节点返回
        if not root:
            return TreeNode(val)
        
        # 定义当前节点指针
        current = root
        
        # 循环查找插入位置
        while current:
            # 如果插入值小于当前节点值
            if val < current.val:
                # 如果左子节点为空，则插入新节点
                if not current.left:
                    current.left = TreeNode(val)
                    break
                else:
                    # 否则继续向左子树查找
                    current = current.left
            else:
                # 如果插入值大于当前节点值
                # 如果右子节点为空，则插入新节点
                if not current.right:
                    current.right = TreeNode(val)
                    break
                else:
                    # 否则继续向右子树查找
                    current = current.right
        
        # 返回根节点
        return root
