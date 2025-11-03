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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 将链表转换为列表以便于处理
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        
        # 使用辅助函数递归构建平衡二叉搜索树
        def build_tree(left, right):
            if left > right:
                return None
            # 选择中间元素作为根节点以确保平衡
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # 递归构建左子树和右子树
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            return root
        
        return build_tree(0, len(nums) - 1)
