import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 使用最大堆来维护前k个最小距离的点
        # 堆中存储元组 (-距离平方, 点坐标)，使用负距离是为了构建最大堆
        heap = []
        
        for point in points:
            x, y = point
            # 计算到原点的距离平方，避免开方运算提高效率
            dist_sq = x*x + y*y
            
            # 如果堆大小小于k，直接加入
            if len(heap) < k:
                heapq.heappush(heap, (-dist_sq, point))
            else:
                # 如果当前点距离小于堆中最大距离，替换堆顶元素
                if dist_sq < -heap[0][0]:
                    heapq.heappushpop(heap, (-dist_sq, point))
        
        # 从堆中提取所有点坐标
        return [point for _, point in heap]
