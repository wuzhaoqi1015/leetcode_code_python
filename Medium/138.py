"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一遍遍历：创建新节点并插入到原节点后面
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        
        # 第二遍遍历：设置新节点的random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 第三遍遍历：分离两个链表
        dummy = Node(0)
        copy_cur = dummy
        cur = head
        while cur:
            copy_cur.next = cur.next
            copy_cur = copy_cur.next
            cur.next = cur.next.next
            cur = cur.next
        
        return dummy.next
