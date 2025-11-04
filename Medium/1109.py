class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 初始化差分数组，长度为n+2以处理边界情况
        diff = [0] * (n + 2)
        
        # 遍历每个预订记录，更新差分数组
        for first, last, seats in bookings:
            diff[first] += seats
            diff[last + 1] -= seats
        
        # 初始化结果数组
        res = [0] * n
        
        # 通过差分数组计算前缀和得到最终结果
        current = 0
        for i in range(1, n + 1):
            current += diff[i]
            res[i - 1] = current
        
        return res
