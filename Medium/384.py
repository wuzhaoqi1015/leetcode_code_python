import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        # 保存原始数组
        self.original = nums[:]
        # 保存当前数组状态
        self.nums = nums[:]

    def reset(self) -> List[int]:
        # 恢复为原始数组
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        # 使用Fisher-Yates洗牌算法进行随机打乱
        n = len(self.nums)
        # 从后往前遍历，每次随机选择一个位置交换
        for i in range(n - 1, 0, -1):
            # 随机生成[0, i]范围内的索引
            j = random.randint(0, i)
            # 交换当前位置和随机位置的值
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
