# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建哑节点，简化头节点删除的情况
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current and current.next:
            # 如果当前节点与下一个节点值相同
            if current.val == current.next.val:
                # 跳过所有重复节点
                while current.next and current.val == current.next.val:
                    current = current.next
                # 将prev的next指向重复节点后的第一个不同节点
                prev.next = current.next
            else:
                # 如果没有重复，移动prev指针
                prev = prev.next
            # 移动current指针
            current = current.next
        
        return dummy.next
