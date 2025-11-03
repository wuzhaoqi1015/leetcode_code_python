class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 首先按照区间的起始位置进行排序
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # 如果合并列表为空，或者当前区间与上一个区间不重叠，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则，将当前区间与上一个区间合并
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
