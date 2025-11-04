class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 按开始时间排序，如果开始时间相同则按结束时间排序
        events.sort(key=lambda x: (x[0], x[1]))
        
        # 使用最小堆来维护当前可参加的会议结束时间
        heap = []
        day = 0
        count = 0
        i = 0
        n = len(events)
        
        # 当还有会议未处理或堆中还有会议时继续
        while i < n or heap:
            # 如果堆为空，跳到下一个会议的开始时间
            if not heap:
                day = events[i][0]
            
            # 将所有开始时间<=当前天数的会议加入堆中
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            # 移除所有结束时间<当前天数的会议（已经无法参加）
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # 如果堆不为空，参加一个结束时间最早的会议
            if heap:
                heapq.heappop(heap)
                count += 1
                day += 1
        
        return count

# 需要导入heapq模块
import heapq
from typing import List
