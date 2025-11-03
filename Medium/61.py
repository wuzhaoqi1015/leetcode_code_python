# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 处理空链表或只有一个节点的链表
        if not head or not head.next:
            return head
            
        # 计算链表长度
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 计算实际需要旋转的次数
        k = k % length
        if k == 0:
            return head
            
        # 找到新的尾节点位置
        new_tail_pos = length - k
        new_tail = head
        for _ in range(new_tail_pos - 1):
            new_tail = new_tail.next
            
        # 重新连接链表
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
