class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 确保start小于destination，方便计算顺时针距离
        if start > destination:
            start, destination = destination, start
        # 计算顺时针方向的距离
        clockwise_dist = sum(distance[start:destination])
        # 计算逆时针方向的距离（总距离减去顺时针距离）
        total_dist = sum(distance)
        counter_clockwise_dist = total_dist - clockwise_dist
        # 返回两个方向中的较小值
        return min(clockwise_dist, counter_clockwise_dist)
