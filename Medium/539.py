class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 将时间转换为分钟数
        minutes = []
        for time in timePoints:
            hour, minute = time.split(':')
            total_minutes = int(hour) * 60 + int(minute)
            minutes.append(total_minutes)
        
        # 排序分钟数列表
        minutes.sort()
        
        # 计算最小时间差，考虑环形时间
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(1, n):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)
        
        # 考虑首尾时间差（环形时间）
        circular_diff = 24 * 60 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
