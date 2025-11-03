# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或只有一个节点，直接返回
        if not head or not head.next:
            return head
        
        # 创建哑节点，简化头节点插入操作
        dummy = ListNode(0)
        dummy.next = head
        
        # 已排序部分的最后一个节点
        last_sorted = head
        # 当前待插入的节点
        curr = head.next
        
        while curr:
            # 如果当前节点值大于等于已排序部分的最后一个节点值
            # 直接将其加入已排序部分
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # 从头开始寻找插入位置
                prev = dummy
                # 找到第一个大于当前节点值的前一个节点
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                # 将当前节点从原位置移除
                last_sorted.next = curr.next
                # 将当前节点插入到正确位置
                curr.next = prev.next
                prev.next = curr
            
            # 移动到下一个待排序节点
            curr = last_sorted.next
        
        return dummy.next
