from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # 计算数组长度
        n = len(arr)
        # 使用Counter统计每个数字的出现频率
        freq = Counter(arr)
        # 按频率从高到低排序
        sorted_freq = sorted(freq.values(), reverse=True)
        
        count = 0
        removed = 0
        # 贪心选择频率最高的数字，直到移除的数量达到数组长度的一半
        for freq_val in sorted_freq:
            removed += freq_val
            count += 1
            if removed >= n // 2:
                break
                
        return count
