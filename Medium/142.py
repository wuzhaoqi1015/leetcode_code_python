# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用快慢指针检测环
        slow = head
        fast = head
        
        # 快指针每次走两步，慢指针每次走一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # 如果快慢指针相遇，说明有环
            if slow == fast:
                # 将慢指针重新指向头节点
                slow = head
                
                # 快慢指针以相同速度前进，相遇点即为环的入口
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        # 无环情况返回None
        return None
