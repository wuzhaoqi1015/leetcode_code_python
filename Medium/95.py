# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def generate(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            # 遍历所有可能的根节点值
            for i in range(start, end + 1):
                # 生成所有可能的左子树
                left_trees = generate(start, i - 1)
                # 生成所有可能的右子树
                right_trees = generate(i + 1, end)
                
                # 将左右子树组合到根节点上
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            return all_trees
        
        return generate(1, n)
