class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 计算时针的角度，每小时30度，每分钟时针移动0.5度
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        # 计算分针的角度，每分钟6度
        minute_angle = minutes * 6
        # 计算两个指针之间的绝对角度差
        angle = abs(hour_angle - minute_angle)
        # 返回较小的角度，即角度差和360度减去角度差中的较小值
        return min(angle, 360 - angle)
