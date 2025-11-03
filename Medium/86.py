# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 创建两个哑节点，分别用于存储小于x和大于等于x的节点
        dummy1 = ListNode(0)  # 小于x的链表头
        dummy2 = ListNode(0)  # 大于等于x的链表头
        # 使用指针分别指向两个链表的当前节点
        p1 = dummy1
        p2 = dummy2
        # 遍历原链表
        current = head
        while current:
            if current.val < x:
                # 将小于x的节点连接到dummy1链表
                p1.next = current
                p1 = p1.next
            else:
                # 将大于等于x的节点连接到dummy2链表
                p2.next = current
                p2 = p2.next
            current = current.next
        # 将两个链表连接起来
        p1.next = dummy2.next
        # 将第二个链表的末尾置为None，避免循环
        p2.next = None
        # 返回新链表的头节点
        return dummy1.next
