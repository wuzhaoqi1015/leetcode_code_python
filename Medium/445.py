# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 使用栈来处理链表，避免翻转链表
        stack1 = []
        stack2 = []
        
        # 将l1的所有节点值压入栈
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # 将l2的所有节点值压入栈
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0  # 进位
        result = None  # 结果链表的头节点
        
        # 当栈不为空或还有进位时继续处理
        while stack1 or stack2 or carry:
            # 从栈中弹出数字，栈为空则取0
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            
            # 计算当前位的和
            total = num1 + num2 + carry
            carry = total // 10  # 计算进位
            digit = total % 10   # 计算当前位的数字
            
            # 创建新节点并连接到结果链表
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
            
        return result
