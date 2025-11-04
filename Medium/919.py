# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        # 初始化队列，找到第一个不完全的节点
        q = deque([root])
        while q:
            node = q.popleft()
            # 如果节点缺少左子节点或右子节点，则加入候选队列
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.queue[0]
        # 如果父节点没有左子节点，插入到左子节点
        if not parent.left:
            parent.left = new_node
        # 如果父节点没有右子节点，插入到右子节点
        else:
            parent.right = new_node
            # 当父节点的左右子节点都满时，从队列中移除
            self.queue.popleft()
        # 将新节点加入候选队列
        self.queue.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
