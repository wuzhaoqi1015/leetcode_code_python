# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 创建虚拟头节点
        current = dummy  # 当前节点指针
        carry = 0  # 进位值
        
        # 遍历两个链表直到都为空且没有进位
        while l1 or l2 or carry:
            # 获取当前节点的值，如果节点为空则为0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算当前位的和（包括进位）
            total = val1 + val2 + carry
            carry = total // 10  # 计算新的进位
            digit = total % 10   # 计算当前位的数字
            
            # 创建新节点并连接到结果链表
            current.next = ListNode(digit)
            current = current.next
            
            # 移动到下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # 返回结果链表的头节点
