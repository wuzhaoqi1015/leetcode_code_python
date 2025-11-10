# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建哑节点，简化头节点删除操作
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # 遍历链表
        while current.next:
            if current.next.val == val:
                # 跳过值为val的节点
                current.next = current.next.next
            else:
                # 移动到下一个节点
                current = current.next
        
        return dummy.next
