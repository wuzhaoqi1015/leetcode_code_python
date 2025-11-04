# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # 使用索引来跟踪当前处理的节点位置
        self.idx = 0
        
        def build_tree(lower_bound, upper_bound):
            # 如果已经处理完所有节点或当前节点值不在有效范围内，返回None
            if self.idx >= len(preorder) or preorder[self.idx] < lower_bound or preorder[self.idx] > upper_bound:
                return None
            
            # 创建当前节点
            current_val = preorder[self.idx]
            node = TreeNode(current_val)
            self.idx += 1
            
            # 递归构建左子树，左子树的值必须小于当前节点值
            node.left = build_tree(lower_bound, current_val - 1)
            
            # 递归构建右子树，右子树的值必须大于当前节点值
            node.right = build_tree(current_val + 1, upper_bound)
            
            return node
        
        # 初始调用，设置值的有效范围为整个整数范围
        return build_tree(float('-inf'), float('inf'))
