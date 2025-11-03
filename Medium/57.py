class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 添加所有在newInterval之前的区间
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 合并与newInterval重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 添加合并后的区间
        result.append(newInterval)
        
        # 添加剩余的区间
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
