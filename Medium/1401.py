class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 找到矩形上距离圆心最近的点
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # 计算最近点到圆心的距离平方
        distance_squared = (closest_x - xCenter) ** 2 + (closest_y - yCenter) ** 2
        
        # 如果距离平方小于等于半径平方，说明有重叠
        return distance_squared <= radius ** 2
