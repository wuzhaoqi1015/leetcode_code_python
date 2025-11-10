# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用迭代方法反转链表
        prev = None  # 前驱节点初始化为None
        curr = head  # 当前节点从链表头开始
        
        # 遍历链表，逐个反转节点指向
        while curr:
            next_temp = curr.next  # 临时保存下一个节点
            curr.next = prev       # 反转当前节点的指向
            prev = curr            # 前驱节点移动到当前位置
            curr = next_temp       # 当前节点移动到下一个位置
        
        # 循环结束后，prev指向反转后的链表头
        return prev
