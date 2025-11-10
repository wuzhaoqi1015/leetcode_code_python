# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            # 将当前节点值加入路径
            if not path:
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)
            
            # 如果是叶子节点，将路径加入结果
            if not node.left and not node.right:
                result.append(path)
                return
            
            # 递归遍历左右子树
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        
        dfs(root, "")
        return result
