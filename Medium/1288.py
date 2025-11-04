class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 按区间起点升序排序，起点相同时按终点降序排序
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0  # 记录被覆盖的区间数量
        max_end = 0  # 记录当前最大的区间终点
        
        # 遍历排序后的区间列表
        for interval in intervals:
            current_end = interval[1]
            # 如果当前区间终点小于等于最大终点，说明被覆盖
            if current_end <= max_end:
                count += 1
            else:
                # 更新最大终点
                max_end = current_end
        
        # 剩余区间数量 = 总区间数 - 被覆盖的区间数
        return len(intervals) - count
