# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        current = head
        # 遍历链表，每次将结果左移一位并加上当前节点的值
        while current:
            result = (result << 1) | current.val
            current = current.next
        return result
