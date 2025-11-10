class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 定义每个月的天数
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # 将日期字符串转换为一年中的第几天
        def date_to_day(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            # 计算前几个月的总天数加上当前月的天数
            return sum(month_days[:month-1]) + day
        
        # 转换所有日期
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)
        
        # 计算重叠区间
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        # 如果存在重叠区间，返回重叠天数；否则返回0
        return max(0, overlap_end - overlap_start + 1)
