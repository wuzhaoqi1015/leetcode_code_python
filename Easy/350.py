from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用Counter统计nums1中每个元素的出现次数
        count1 = Counter(nums1)
        result = []
        
        # 遍历nums2中的每个元素
        for num in nums2:
            # 如果元素在count1中存在且计数大于0
            if count1.get(num, 0) > 0:
                result.append(num)  # 将元素添加到结果中
                count1[num] -= 1    # 减少count1中该元素的计数
        
        return result
