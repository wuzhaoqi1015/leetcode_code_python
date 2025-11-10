import heapq
from math import isqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 使用最大堆，Python的heapq默认是最小堆，所以存储负值
        max_heap = []
        for gift in gifts:
            heapq.heappush(max_heap, -gift)
        
        # 执行k次操作
        for _ in range(k):
            # 弹出当前最大的礼物堆
            max_gift = -heapq.heappop(max_heap)
            # 计算平方根并向下取整
            new_gift = isqrt(max_gift)
            # 将新值推回堆中
            heapq.heappush(max_heap, -new_gift)
        
        # 计算剩余礼物总数
        total = 0
        for gift in max_heap:
            total += -gift
        
        return total
