"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        dummy = Node(0, None, head, None)  # 创建虚拟头节点简化边界处理
        prev = dummy
        stack = [head]  # 使用栈来深度优先遍历链表
        
        while stack:
            curr = stack.pop()
            
            # 连接当前节点到前一个节点
            prev.next = curr
            curr.prev = prev
            
            # 如果存在下一个节点，先压入栈中
            if curr.next:
                stack.append(curr.next)
            
            # 如果存在子节点，压入栈中（后进先出，子节点会先处理）
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # 清空子指针
            
            prev = curr
        
        # 断开虚拟头节点与真实头节点的连接
        dummy.next.prev = None
        return dummy.next
