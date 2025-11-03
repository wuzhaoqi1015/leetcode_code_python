# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建哑节点，简化头节点处理
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 遍历链表，每次处理两个节点
        while prev.next and prev.next.next:
            # 获取当前要交换的两个节点
            first = prev.next
            second = prev.next.next
            
            # 执行交换操作
            first.next = second.next
            second.next = first
            prev.next = second
            
            # 移动prev指针到下一对的前一个位置
            prev = first
        
        return dummy.next
