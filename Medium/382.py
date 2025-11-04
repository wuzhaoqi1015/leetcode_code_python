# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head  # 存储链表头节点

    def getRandom(self) -> int:
        count = 0
        current = self.head
        result = None
        
        # 使用水库抽样算法，保证每个节点被选中的概率相等
        while current:
            count += 1
            # 以1/count的概率选择当前节点
            if random.randint(1, count) == 1:
                result = current.val
            current = current.next
            
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
