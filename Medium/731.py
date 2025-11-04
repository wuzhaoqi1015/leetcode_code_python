class MyCalendarTwo:

    def __init__(self):
        # 存储所有已预订的区间
        self.bookings = []
        # 存储已经双重预订的区间（重叠两次的区间）
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        # 检查新预订是否会与已双重预订的区间产生三重预订
        for start, end in self.overlaps:
            if startTime < end and endTime > start:
                # 与某个双重预订区间重叠，会产生三重预订
                return False
        
        # 检查新预订与所有已预订区间的重叠情况
        for start, end in self.bookings:
            if startTime < end and endTime > start:
                # 计算重叠区间
                overlap_start = max(startTime, start)
                overlap_end = min(endTime, end)
                # 将重叠区间加入双重预订列表
                self.overlaps.append((overlap_start, overlap_end))
        
        # 将新预订加入已预订列表
        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
