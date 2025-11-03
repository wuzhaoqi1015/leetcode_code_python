# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []  # 存储所有符合条件的路径
        current_path = []  # 存储当前遍历路径
        
        def dfs(node, remaining):
            if not node:
                return
                
            current_path.append(node.val)  # 将当前节点加入路径
            
            # 检查是否为叶子节点且路径和等于目标值
            if not node.left and not node.right and remaining == node.val:
                result.append(current_path[:])  # 添加路径的副本到结果中
            
            # 递归遍历左右子树
            dfs(node.left, remaining - node.val)
            dfs(node.right, remaining - node.val)
            
            current_path.pop()  # 回溯，移除当前节点
        
        dfs(root, targetSum)
        return result
