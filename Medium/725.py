# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 计算链表长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # 计算每个部分的基础长度和需要额外增加一个节点的部分数量
        base_length = length // k
        extra = length % k
        
        result = []
        curr = head
        
        for i in range(k):
            # 当前部分的头节点
            part_head = curr
            
            # 计算当前部分的长度
            part_size = base_length
            if i < extra:
                part_size += 1
            
            # 移动到当前部分的末尾
            for j in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            # 断开链表并记录下一部分的头节点
            if curr:
                next_head = curr.next
                curr.next = None
                curr = next_head
            
            # 将当前部分加入结果
            result.append(part_head)
        
        return result
