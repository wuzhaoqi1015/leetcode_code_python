class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 创建差分数组，由于位置范围是0到1000，所以数组大小为1001
        diff = [0] * 1001
        
        # 遍历每个行程，在from位置增加乘客数，在to位置减少乘客数
        for num_passengers, from_loc, to_loc in trips:
            diff[from_loc] += num_passengers
            diff[to_loc] -= num_passengers
        
        # 当前乘客数量
        current_passengers = 0
        
        # 遍历所有位置，计算每个位置的乘客数量
        for i in range(1001):
            current_passengers += diff[i]
            # 如果任何位置的乘客数量超过容量，返回False
            if current_passengers > capacity:
                return False
        
        # 所有位置都满足容量要求，返回True
        return True
