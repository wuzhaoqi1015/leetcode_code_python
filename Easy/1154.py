class Solution:
    def dayOfYear(self, date: str) -> int:
        # 分割日期字符串为年、月、日
        year, month, day = map(int, date.split('-'))
        
        # 定义每个月的天数，二月默认28天
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # 判断是否为闰年，闰年二月有29天
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29
        
        # 计算总天数：前month-1个月的天数之和加上当前月的天数
        total_days = sum(days_in_month[:month-1]) + day
        
        return total_days
