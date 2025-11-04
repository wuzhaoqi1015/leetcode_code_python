# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        
        # 使用字典记录每个序列出现的次数
        subtree_count = defaultdict(int)
        # 存储结果的列表
        result = []
        
        def serialize(node):
            if not node:
                return "#"
            
            # 序列化当前子树
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            
            # 构建当前子树的序列化字符串
            subtree_serial = f"{node.val},{left_serial},{right_serial}"
            
            # 检查该序列是否已经出现过
            subtree_count[subtree_serial] += 1
            
            # 如果出现次数为2，说明找到了重复子树，将当前节点加入结果
            if subtree_count[subtree_serial] == 2:
                result.append(node)
            
            return subtree_serial
        
        serialize(root)
        return result
