class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 计算两点之间距离的平方，避免浮点数精度问题
        def distance_sq(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        
        # 收集所有点对之间的距离平方
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i+1, 4):
                dist_sq = distance_sq(points[i], points[j])
                distances.append(dist_sq)
        
        # 对距离进行排序
        distances.sort()
        
        # 正方形应该有：4条相等的边（最短距离），2条相等的对角线（最长距离）
        # 且对角线长度应该是边长的√2倍，这里用平方比较：对角线平方 = 2 * 边平方
        # 同时要确保没有距离为0的点（即没有重合点）
        if distances[0] > 0 and distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and distances[4] == 2 * distances[0]:
            return True
        return False
