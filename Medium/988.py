# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # 初始化最小字符串为None，用于后续比较
        self.min_str = None
        
        def dfs(node, current_path):
            if not node:
                return
            
            # 将当前节点的值转换为对应字符，并添加到路径开头
            current_path = chr(node.val + ord('a')) + current_path
            
            # 如果是叶子节点
            if not node.left and not node.right:
                # 如果是第一个找到的字符串或者当前字符串更小，则更新最小字符串
                if self.min_str is None or current_path < self.min_str:
                    self.min_str = current_path
                return
            
            # 递归遍历左子树
            if node.left:
                dfs(node.left, current_path)
            
            # 递归遍历右子树
            if node.right:
                dfs(node.right, current_path)
        
        # 从根节点开始深度优先搜索，初始路径为空字符串
        dfs(root, "")
        
        return self.min_str
