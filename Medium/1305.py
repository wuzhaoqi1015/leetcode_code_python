# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # 中序遍历二叉搜索树得到有序列表
        def inorder_traversal(root, result):
            if root is None:
                return
            inorder_traversal(root.left, result)
            result.append(root.val)
            inorder_traversal(root.right, result)
        
        # 获取两棵树的中序遍历结果
        list1 = []
        list2 = []
        inorder_traversal(root1, list1)
        inorder_traversal(root2, list2)
        
        # 合并两个有序列表
        merged = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # 添加剩余元素
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        return merged
