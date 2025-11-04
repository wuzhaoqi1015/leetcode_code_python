# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_map = {}
        current = dummy
        
        # 第一次遍历，记录每个前缀和对应的节点
        while current:
            prefix_sum += current.val
            prefix_map[prefix_sum] = current
            current = current.next
        
        # 第二次遍历，删除和为0的连续节点序列
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            # 如果当前前缀和在map中存在，说明中间有和为0的序列
            if prefix_sum in prefix_map:
                current.next = prefix_map[prefix_sum].next
            current = current.next
        
        return dummy.next
