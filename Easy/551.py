class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0  # 统计缺勤次数
        late_streak = 0   # 统计连续迟到天数
        
        for char in s:
            if char == 'A':
                absent_count += 1
                late_streak = 0  # 缺勤会打断连续迟到
                # 如果缺勤达到2次，直接返回False
                if absent_count >= 2:
                    return False
            elif char == 'L':
                late_streak += 1
                # 如果连续迟到达到3天，直接返回False
                if late_streak >= 3:
                    return False
            else:  # char == 'P'
                late_streak = 0  # 到场会打断连续迟到
        
        # 如果通过所有检查，返回True
        return True
