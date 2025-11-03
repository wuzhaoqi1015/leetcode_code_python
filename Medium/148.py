# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 处理空链表或单节点链表的边界情况
        if not head or not head.next:
            return head
        
        # 使用归并排序对链表进行排序
        # 第一步：找到链表的中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 将链表分为两部分
        mid = slow.next
        slow.next = None
        
        # 递归排序左右两部分
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并两个有序链表
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # 将剩余节点连接到已排序链表的末尾
        current.next = left if left else right
        
        return dummy.next
