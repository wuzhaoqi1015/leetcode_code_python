from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 使用Counter统计每个数字出现的频率
        count = Counter(nums)
        # 使用最小堆来维护频率最高的k个元素
        heap = []
        # 遍历频率字典中的每个元素
        for num, freq in count.items():
            # 将元素和频率作为元组存入堆中，注意堆按频率排序
            heapq.heappush(heap, (freq, num))
            # 如果堆的大小超过k，则弹出频率最小的元素
            if len(heap) > k:
                heapq.heappop(heap)
        # 从堆中提取所有元素，返回数字部分
        return [num for freq, num in heap]
