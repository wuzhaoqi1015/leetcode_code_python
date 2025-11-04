class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # 存储每个区间的起始点和原始索引
        starts = [(intervals[i][0], i) for i in range(n)]
        # 按起始点排序
        starts.sort()
        
        result = []
        for i in range(n):
            end_i = intervals[i][1]
            # 二分查找找到第一个起始点 >= end_i 的区间
            left, right = 0, n - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if starts[mid][0] >= end_i:
                    idx = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(idx)
        
        return result
