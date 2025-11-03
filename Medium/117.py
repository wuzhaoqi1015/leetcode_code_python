class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # 使用已建立的next指针来遍历
        leftmost = root
        
        while leftmost:
            # 当前层的遍历指针
            curr = leftmost
            # 下一层的起始节点和前一个节点
            prev = None
            leftmost = None
            
            while curr:
                # 处理左子节点
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        leftmost = curr.left
                    prev = curr.left
                
                # 处理右子节点
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        leftmost = curr.right
                    prev = curr.right
                
                # 移动到当前层的下一个节点
                curr = curr.next
        
        return root
