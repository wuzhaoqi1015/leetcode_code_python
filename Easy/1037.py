class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 提取三个点的坐标
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # 检查是否有重复的点
        if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
            return False
        
        # 计算向量叉积来判断三点是否共线
        # 向量AB = (x2-x1, y2-y1), 向量AC = (x3-x1, y3-y1)
        # 叉积 = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
        cross_product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        
        # 如果叉积不为0，说明三点不共线
        return cross_product != 0
