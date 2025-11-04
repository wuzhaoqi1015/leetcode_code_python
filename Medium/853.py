class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 创建车辆信息列表，每个元素为(位置, 到达终点所需时间)
        cars = []
        n = len(position)
        for i in range(n):
            # 计算每辆车到达终点所需时间
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        # 按位置从大到小排序（离终点近的在前）
        cars.sort(key=lambda x: x[0], reverse=True)
        
        fleet_count = 0
        current_max_time = -1.0
        
        # 遍历所有车辆
        for i in range(n):
            # 如果当前车辆到达终点的时间大于前面的最大时间，说明会形成新的车队
            if cars[i][1] > current_max_time:
                fleet_count += 1
                current_max_time = cars[i][1]
        
        return fleet_count
