import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        # 使用字典存储每个值对应的所有索引
        self.index_map = {}
        for idx, num in enumerate(nums):
            if num not in self.index_map:
                self.index_map[num] = []
            self.index_map[num].append(idx)

    def pick(self, target: int) -> int:
        # 从目标值的索引列表中随机选择一个返回
        indices = self.index_map.get(target, [])
        return random.choice(indices) if indices else -1

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
