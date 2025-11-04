# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 使用字典存储后序遍历中值对应的索引，便于快速查找
        post_index_map = {}
        for idx, val in enumerate(postorder):
            post_index_map[val] = idx
        
        def build(pre_start, pre_end, post_start, post_end):
            # 递归终止条件：没有节点需要处理
            if pre_start > pre_end:
                return None
            # 创建当前根节点，前序遍历第一个元素即为根节点
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            # 如果只有一个节点，直接返回
            if pre_start == pre_end:
                return root
            
            # 找到左子树的根节点在后序遍历中的位置
            left_root_val = preorder[pre_start + 1]
            left_root_post_index = post_index_map[left_root_val]
            
            # 计算左子树的节点数量
            left_size = left_root_post_index - post_start + 1
            
            # 递归构建左子树
            # 前序遍历中左子树范围：[pre_start+1, pre_start+left_size]
            # 后序遍历中左子树范围：[post_start, left_root_post_index]
            root.left = build(pre_start + 1, pre_start + left_size, 
                            post_start, left_root_post_index)
            
            # 递归构建右子树
            # 前序遍历中右子树范围：[pre_start+left_size+1, pre_end]
            # 后序遍历中右子树范围：[left_root_post_index+1, post_end-1]
            root.right = build(pre_start + left_size + 1, pre_end,
                             left_root_post_index + 1, post_end - 1)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
