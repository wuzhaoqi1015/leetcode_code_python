# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # 真二叉树的节点数必须是奇数
        if n % 2 == 0:
            return []
        
        # 使用记忆化存储已计算的结果
        memo = {}
        
        def generate_trees(num_nodes):
            # 如果已经计算过，直接返回结果
            if num_nodes in memo:
                return memo[num_nodes]
            
            trees = []
            # 基本情况：只有一个节点
            if num_nodes == 1:
                trees.append(TreeNode(0))
                memo[num_nodes] = trees
                return trees
            
            # 遍历所有可能的左右子树节点分配
            # 左子树节点数从1开始，每次增加2（因为必须是奇数）
            for left_nodes in range(1, num_nodes, 2):
                right_nodes = num_nodes - 1 - left_nodes  # 减去根节点
                
                # 递归生成所有可能的左右子树
                left_trees = generate_trees(left_nodes)
                right_trees = generate_trees(right_nodes)
                
                # 组合所有可能的左右子树对
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            
            memo[num_nodes] = trees
            return trees
        
        return generate_trees(n)
