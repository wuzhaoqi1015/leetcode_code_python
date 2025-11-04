class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 使用二分查找来寻找最小速度
        left, right = 1, max(piles)  # 最小速度为1，最大速度为最大堆的香蕉数
        
        # 定义计算总时间的函数
        def calculate_time(speed):
            total_time = 0
            for pile in piles:
                # 每堆香蕉需要的时间是 pile / speed 向上取整
                total_time += (pile + speed - 1) // speed
            return total_time
        
        # 二分查找
        while left < right:
            mid = (left + right) // 2
            # 计算以当前速度mid需要的时间
            time_needed = calculate_time(mid)
            
            if time_needed <= h:
                # 如果时间足够，尝试更小的速度
                right = mid
            else:
                # 如果时间不够，需要更大的速度
                left = mid + 1
        
        return left
