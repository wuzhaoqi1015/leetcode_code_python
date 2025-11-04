# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # 深度优先搜索函数，检查从当前树节点开始的路径是否匹配链表
        def dfs(node: TreeNode, list_node: ListNode) -> bool:
            # 如果链表节点为空，说明链表已全部匹配完成
            if not list_node:
                return True
            # 如果树节点为空或值不匹配，返回False
            if not node or node.val != list_node.val:
                return False
            # 递归检查左子树或右子树是否匹配链表的下一个节点
            return dfs(node.left, list_node.next) or dfs(node.right, list_node.next)
        
        # 如果树节点为空，返回False
        if not root:
            return False
        # 检查当前树节点开始的路径是否匹配链表，或者递归检查左子树或右子树
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
