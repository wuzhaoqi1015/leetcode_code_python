class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')  # 初始化最小距离为无穷大
        min_index = -1  # 初始化最小下标为-1
        
        for idx, point in enumerate(points):
            a, b = point  # 解构当前点的坐标
            # 检查是否为有效点（x坐标相同或y坐标相同）
            if a == x or b == y:
                # 计算曼哈顿距离
                distance = abs(a - x) + abs(b - y)
                # 如果找到更小的距离，更新最小距离和下标
                if distance < min_distance:
                    min_distance = distance
                    min_index = idx
                # 如果距离相等但下标更小，更新下标
                elif distance == min_distance and idx < min_index:
                    min_index = idx
        
        return min_index
