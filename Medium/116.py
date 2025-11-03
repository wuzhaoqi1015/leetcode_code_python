class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                # 连接同一个父节点的左右子节点
                head.left.next = head.right
                # 连接不同父节点的相邻子节点
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            # 移动到下一层的最左节点
            leftmost = leftmost.left
        
        return root
