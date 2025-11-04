class UndergroundSystem:

    def __init__(self):
        # 存储乘客进站信息：id -> (stationName, t)
        self.check_in_data = {}
        # 存储行程统计信息：(startStation, endStation) -> (total_time, count)
        self.journey_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # 记录乘客进站信息
        self.check_in_data[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # 获取乘客进站信息
        start_station, start_time = self.check_in_data[id]
        # 计算行程时间
        travel_time = t - start_time
        # 行程键
        journey_key = (start_station, stationName)
        
        # 更新行程统计
        if journey_key in self.journey_data:
            total_time, count = self.journey_data[journey_key]
            self.journey_data[journey_key] = (total_time + travel_time, count + 1)
        else:
            self.journey_data[journey_key] = (travel_time, 1)
        
        # 移除已完成的进站记录
        del self.check_in_data[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # 获取行程统计信息
        journey_key = (startStation, endStation)
        total_time, count = self.journey_data[journey_key]
        # 计算平均时间
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
