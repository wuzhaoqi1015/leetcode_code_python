import random
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.used = set()  # 存储已经被选中的位置索引

    def flip(self) -> List[int]:
        # 如果所有位置都被使用过，直接返回空（根据题目保证至少有一个0）
        if len(self.used) == self.total:
            return []
        
        # 随机选择一个位置索引
        idx = random.randint(0, self.total - 1)
        # 如果该位置已经被使用，继续随机选择直到找到未使用的位置
        while idx in self.used:
            idx = random.randint(0, self.total - 1)
        
        # 标记该位置为已使用
        self.used.add(idx)
        # 将一维索引转换为二维坐标
        i = idx // self.n
        j = idx % self.n
        return [i, j]

    def reset(self) -> None:
        # 重置时清空所有已使用标记
        self.used.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
