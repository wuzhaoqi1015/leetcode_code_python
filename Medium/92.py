# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 创建虚拟头节点，简化边界处理
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 移动到left位置的前一个节点
        for _ in range(left - 1):
            prev = prev.next
        
        # 开始反转的起始节点
        curr = prev.next
        
        # 反转从left到right的部分
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
