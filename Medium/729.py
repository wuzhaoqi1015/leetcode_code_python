class MyCalendar:

    def __init__(self):
        # 使用列表存储所有已预订的区间
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        # 遍历所有已存在的区间
        for event in self.events:
            # 检查新区间与已存在区间是否有重叠
            # 重叠条件：新开始时间小于已存在区间的结束时间，且新结束时间大于已存在区间的开始时间
            if startTime < event[1] and endTime > event[0]:
                return False
        # 如果没有重叠，添加新区间并返回True
        self.events.append([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
