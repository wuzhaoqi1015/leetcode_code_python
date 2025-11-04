class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 如果区间为空，直接返回0
        if not intervals:
            return 0
            
        # 按照区间右端点进行排序
        intervals.sort(key=lambda x: x[1])
        
        # 初始化计数器，记录不重叠区间的数量
        count = 1
        # 记录当前选择的区间的右端点
        end_pos = intervals[0][1]
        
        # 遍历排序后的区间
        for i in range(1, len(intervals)):
            # 如果当前区间的左端点大于等于前一个区间的右端点，说明不重叠
            if intervals[i][0] >= end_pos:
                count += 1
                end_pos = intervals[i][1]
        
        # 需要移除的区间数量 = 总区间数 - 不重叠区间数
        return len(intervals) - count
