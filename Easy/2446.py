class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # 将时间字符串转换为分钟数进行比较
        def time_to_minutes(time_str):
            hours, minutes = time_str.split(':')
            return int(hours) * 60 + int(minutes)
        
        # 转换所有时间点
        start1 = time_to_minutes(event1[0])
        end1 = time_to_minutes(event1[1])
        start2 = time_to_minutes(event2[0])
        end2 = time_to_minutes(event2[1])
        
        # 检查两个时间段是否有重叠
        # 如果没有冲突，应该是 event1 完全在 event2 之前或之后
        # 即 end1 < start2 或 end2 < start1
        # 所以有冲突的情况就是取反
        return not (end1 < start2 or end2 < start1)
