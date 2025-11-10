class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 已知1971年1月1日是星期五
        base_year = 1971
        base_day = 5  # 0=Sunday, 1=Monday, ..., 5=Friday, 6=Saturday
        
        # 计算从1971年1月1日到目标日期的总天数
        total_days = 0
        
        # 计算从1971年到year-1年的总天数
        for y in range(base_year, year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                total_days += 366
            else:
                total_days += 365
        
        # 计算当年1月到month-1月的总天数
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(1, month):
            total_days += month_days[m-1]
            # 如果是闰年且月份大于2月，需要加1天
            if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                total_days += 1
        
        # 加上当月的天数
        total_days += day - 1  # 减去1因为1月1日是第0天
        
        # 计算星期几
        day_of_week = (base_day + total_days) % 7
        
        # 映射到对应的星期字符串
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        return week_days[day_of_week]
