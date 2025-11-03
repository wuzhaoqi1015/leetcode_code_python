# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 创建中序遍历值到索引的映射，便于快速定位根节点位置
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            # 递归终止条件：先序遍历区间为空
            if pre_start > pre_end:
                return None
            
            # 当前子树的根节点是先序遍历的第一个元素
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            root_idx = inorder_map[root_val]
            
            # 计算左子树的节点数量
            left_size = root_idx - in_start
            
            # 递归构建左子树
            # 左子树的先序遍历区间：[pre_start+1, pre_start+left_size]
            # 左子树的中序遍历区间：[in_start, root_idx-1]
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            
            # 递归构建右子树
            # 右子树的先序遍历区间：[pre_start+left_size+1, pre_end]
            # 右子树的中序遍历区间：[root_idx+1, in_end]
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
            
            return root
        
        # 调用递归函数，初始区间为整个数组
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
