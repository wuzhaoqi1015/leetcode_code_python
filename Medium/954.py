from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 统计每个数字出现的频率
        count = Counter(arr)
        
        # 按绝对值从小到大排序，确保先处理较小的数字
        sorted_keys = sorted(arr, key=lambda x: abs(x))
        
        for num in sorted_keys:
            # 如果当前数字已经被使用完，跳过
            if count[num] == 0:
                continue
                
            # 如果当前数字的两倍不存在或数量不足，返回False
            if count[2 * num] < count[num]:
                return False
                
            # 更新两倍数字的计数
            count[2 * num] -= count[num]
            # 当前数字计数清零
            count[num] = 0
            
        return True
