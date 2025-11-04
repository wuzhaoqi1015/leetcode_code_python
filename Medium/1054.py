from collections import Counter
import heapq
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 统计每个条形码的出现频率
        count = Counter(barcodes)
        
        # 使用最大堆，按频率从高到低排列
        # 堆中存储元组 (-频率, 条形码值)
        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-freq, num))
        
        result = []
        prev_num = None
        prev_freq = 0
        
        while max_heap:
            # 取出当前频率最高的条形码
            curr_freq, curr_num = heapq.heappop(max_heap)
            
            # 将当前条形码加入结果
            result.append(curr_num)
            
            # 如果前一个条形码还有剩余，重新放回堆中
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_num))
            
            # 更新前一个条形码的信息
            prev_num = curr_num
            prev_freq = curr_freq + 1  # 频率减1（因为是负数，所以+1）
        
        return result
