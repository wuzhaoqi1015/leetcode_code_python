import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 初始化最小堆
        heap = []
        m, n = len(nums1), len(nums2)
        
        # 将nums1中每个元素与nums2的第一个元素配对入堆
        for i in range(min(m, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        # 当堆不为空且结果数量小于k时继续
        while heap and len(result) < k:
            # 弹出当前最小和的对
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # 如果当前nums2索引还有下一个元素，将下一个配对入堆
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
