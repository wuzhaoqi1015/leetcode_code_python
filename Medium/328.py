# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        odd = head  # 奇数节点链表的头
        even = head.next  # 偶数节点链表的头
        even_head = even  # 保存偶数链表的头用于后续连接
        
        # 遍历链表，分离奇偶节点
        while even and even.next:
            odd.next = even.next  # 奇数节点指向下一个奇数节点
            odd = odd.next  # 移动奇数指针
            even.next = odd.next  # 偶数节点指向下一个偶数节点
            even = even.next  # 移动偶数指针
            
        odd.next = even_head  # 将偶数链表连接到奇数链表后面
        return head
