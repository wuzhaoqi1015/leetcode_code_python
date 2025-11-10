from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 统计每个数字出现的频率
        freq = Counter(nums)
        
        # 自定义排序规则：先按频率升序，频率相同则按数值降序
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums
