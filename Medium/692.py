from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 统计每个单词的出现频率
        count = Counter(words)
        
        # 使用最小堆来维护前k个最频繁的单词
        # 堆中存储元组(-频率, 单词)，这样频率高的会排在前面
        # 当频率相同时，按字典序排序（Python中字符串默认按字典序）
        heap = []
        for word, freq in count.items():
            # 使用负频率使得堆变成最大堆的效果
            heapq.heappush(heap, (-freq, word))
        
        # 从堆中取出前k个元素
        result = []
        for _ in range(k):
            # 弹出频率最高（负值最小）的单词
            freq, word = heapq.heappop(heap)
            result.append(word)
        
        return result
