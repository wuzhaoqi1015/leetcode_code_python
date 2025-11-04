# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # 将删除列表转换为集合，提高查找效率
        delete_set = set(to_delete)
        # 存储森林结果的列表
        forest = []
        
        def dfs(node, is_root):
            # 如果节点为空，返回None
            if not node:
                return None
                
            # 标记当前节点是否需要删除
            to_be_deleted = node.val in delete_set
            
            # 如果是根节点且不需要删除，则加入森林
            if is_root and not to_be_deleted:
                forest.append(node)
                
            # 递归处理左右子树
            # 如果当前节点被删除，那么子节点将成为新的根节点
            node.left = dfs(node.left, to_be_deleted)
            node.right = dfs(node.right, to_be_deleted)
            
            # 如果当前节点需要删除，返回None；否则返回当前节点
            return None if to_be_deleted else node
            
        # 从根节点开始遍历，根节点默认为根
        dfs(root, True)
        return forest
