# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 创建中序遍历值到索引的映射，便于快速查找根节点位置
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            # 递归终止条件：没有节点需要处理
            if in_start > in_end or post_start > post_end:
                return None
            
            # 后序遍历的最后一个元素是当前子树的根节点
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            root_index = inorder_index_map[root_val]
            
            # 计算左子树的节点数量
            left_size = root_index - in_start
            
            # 递归构建左子树
            # 左子树在中序遍历中的范围：[in_start, root_index-1]
            # 左子树在后序遍历中的范围：[post_start, post_start+left_size-1]
            root.left = build(in_start, root_index - 1, post_start, post_start + left_size - 1)
            
            # 递归构建右子树
            # 右子树在中序遍历中的范围：[root_index+1, in_end]
            # 右子树在后序遍历中的范围：[post_start+left_size, post_end-1]
            root.right = build(root_index + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        # 初始调用，处理整个数组范围
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
