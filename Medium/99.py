# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 使用Morris中序遍历，O(1)空间复杂度
        current = root
        prev = None
        first = None
        second = None
        
        while current:
            if current.left is None:
                # 处理当前节点
                if prev and prev.val > current.val:
                    if first is None:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                # 找到前驱节点
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # 建立临时链接
                    predecessor.right = current
                    current = current.left
                else:
                    # 恢复树结构并处理当前节点
                    predecessor.right = None
                    if prev and prev.val > current.val:
                        if first is None:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
        
        # 交换两个错误节点的值
        if first and second:
            first.val, second.val = second.val, first.val
