class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 如果只有两个点，直接返回True
        if len(coordinates) == 2:
            return True
            
        # 获取前两个点的坐标
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        # 计算前两个点确定的直线斜率
        # 为了避免除零错误，使用乘法形式判断三点共线
        # 即判断 (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)
        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i]
            # 如果任意三点不共线，返回False
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
                
        # 所有点都在同一直线上
        return True
