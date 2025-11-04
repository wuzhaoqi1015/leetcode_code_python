class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # 如果quadTree1是叶子节点
        if quadTree1.isLeaf:
            # 如果quadTree1的值为1，或运算结果总是1，返回quadTree1
            if quadTree1.val:
                return Node(True, True, None, None, None, None)
            # 如果quadTree1的值为0，或运算结果等于quadTree2的值，返回quadTree2
            else:
                return quadTree2
        # 如果quadTree2是叶子节点
        if quadTree2.isLeaf:
            # 如果quadTree2的值为1，或运算结果总是1，返回quadTree2
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            # 如果quadTree2的值为0，或运算结果等于quadTree1的值，返回quadTree1
            else:
                return quadTree1
        
        # 两个节点都不是叶子节点，递归处理四个子区域
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # 检查四个子节点是否都是叶子节点且值相同
        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            # 如果四个子节点值相同，合并为一个叶子节点
            return Node(topLeft.val, True, None, None, None, None)
        else:
            # 否则返回非叶子节点，val可以任意设置，这里设为False
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
