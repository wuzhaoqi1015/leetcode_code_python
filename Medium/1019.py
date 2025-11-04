# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 将链表转换为列表，便于处理
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        n = len(values)
        result = [0] * n  # 初始化结果数组，默认值为0
        stack = []  # 使用单调栈存储索引
        
        # 遍历链表值
        for i in range(n):
            # 当栈不为空且当前值大于栈顶索引对应的值时
            while stack and values[i] > values[stack[-1]]:
                # 弹出栈顶索引，设置对应位置的结果为当前值
                idx = stack.pop()
                result[idx] = values[i]
            # 将当前索引入栈
            stack.append(i)
        
        return result
