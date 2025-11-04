class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []  # 存储已占用的座位编号，保持有序

    def seat(self) -> int:
        if not self.seats:
            # 如果考场为空，学生坐在0号座位
            self.seats.append(0)
            return 0
        
        # 计算第一个座位到0的距离
        max_dist = self.seats[0]
        idx = 0  # 记录插入位置
        seat_to_add = 0  # 记录要添加的座位编号
        
        # 遍历已占用座位之间的间隔
        for i in range(1, len(self.seats)):
            # 计算当前间隔的距离
            dist = (self.seats[i] - self.seats[i-1]) // 2
            # 如果找到更大的距离，或者距离相同但座位编号更小
            if dist > max_dist or (dist == max_dist and self.seats[i-1] + dist < seat_to_add):
                max_dist = dist
                seat_to_add = self.seats[i-1] + dist
                idx = i
        
        # 检查最后一个座位到末尾的距离
        last_dist = self.n - 1 - self.seats[-1]
        if last_dist > max_dist:
            seat_to_add = self.n - 1
            idx = len(self.seats)
        
        # 插入座位并保持有序
        self.seats.insert(idx, seat_to_add)
        return seat_to_add

    def leave(self, p: int) -> None:
        # 从已占用座位列表中移除p
        self.seats.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
