# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.index = 0  # 记录当前遍历到voyage的索引
        self.result = []  # 存储需要翻转的节点值
        
        def dfs(node):
            if not node:
                return True
            # 如果当前节点值与voyage不匹配，直接返回False
            if node.val != voyage[self.index]:
                return False
            self.index += 1
            
            # 如果左子树存在且与voyage不匹配，尝试翻转
            if node.left and node.left.val != voyage[self.index]:
                # 翻转当前节点
                self.result.append(node.val)
                # 翻转后先遍历右子树，再遍历左子树
                return dfs(node.right) and dfs(node.left)
            else:
                # 正常遍历：先左子树，后右子树
                return dfs(node.left) and dfs(node.right)
        
        if dfs(root):
            return self.result
        else:
            return [-1]
