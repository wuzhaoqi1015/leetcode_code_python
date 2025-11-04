from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        # 使用最小堆，存储分数和对应的分子分母索引
        heap = []
        # 初始化堆，对于每个分母，存储最小的分数（分子为第一个元素）
        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))
        
        # 弹出k-1个最小元素
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            # 如果当前分子不是最后一个，将下一个分子与相同分母的分数加入堆
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))
        
        # 第k个最小分数
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
