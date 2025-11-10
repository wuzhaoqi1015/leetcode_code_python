class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        # 遍历所有相邻点对
        for i in range(len(points) - 1):
            # 计算当前点与下一个点的坐标差
            dx = abs(points[i][0] - points[i+1][0])
            dy = abs(points[i][1] - points[i+1][1])
            # 最小时间等于对角移动次数加上直线移动次数
            # 对角移动次数等于min(dx, dy)，直线移动次数等于abs(dx - dy)
            total_time += max(dx, dy)
        return total_time
