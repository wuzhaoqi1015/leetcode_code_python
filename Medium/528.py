import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        # 构建前缀和数组
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # 生成一个在 [1, total_sum] 范围内的随机数
        target = random.randint(1, self.total_sum)
        
        # 使用二分查找找到第一个大于等于 target 的前缀和
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
