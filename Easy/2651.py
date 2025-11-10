class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # 计算总时间并对24取模，得到24小时制下的实际到站时间
        total_time = arrivalTime + delayedTime
        return total_time % 24
