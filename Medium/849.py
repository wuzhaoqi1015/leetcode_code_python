class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [n] * n  # 初始化左侧最近有人座位的距离
        right = [n] * n  # 初始化右侧最近有人座位的距离
        
        # 从左向右扫描，计算每个位置到左侧最近有人座位的距离
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
        
        # 从右向左扫描，计算每个位置到右侧最近有人座位的距离
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n-1:
                right[i] = right[i+1] + 1
        
        # 遍历所有座位，取左右距离的最小值，然后找出最大值
        max_dist = 0
        for i in range(n):
            if seats[i] == 0:
                # 当前空座位到最近有人座位的距离是左右距离中的较小值
                dist = min(left[i], right[i])
                max_dist = max(max_dist, dist)
        
        return max_dist
