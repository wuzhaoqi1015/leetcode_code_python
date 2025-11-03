# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建哑节点作为合并后链表的起始点
        dummy = ListNode(-1)
        current = dummy
        
        # 遍历两个链表，比较节点值
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 将剩余的非空链表连接到当前链表末尾
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # 返回合并后链表的头节点（跳过哑节点）
        return dummy.next
