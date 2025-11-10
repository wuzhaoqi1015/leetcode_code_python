class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 使用最大堆模拟过程，Python的heapq默认是最小堆，所以用负数存储
        import heapq
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # 取出两个最大的石头
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            # 如果重量不同，将差值重新放入堆中
            if first != second:
                new_stone = first - second
                heapq.heappush(max_heap, -new_stone)
        
        # 如果堆中还有石头，返回其重量；否则返回0
        return -max_heap[0] if max_heap else 0
