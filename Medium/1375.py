class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_index = 0  # 记录当前遇到的最大翻转位置
        count = 0  # 记录前缀一致的次数
        for step, pos in enumerate(flips, 1):  # 从第1步开始遍历
            if pos > max_index:  # 更新最大翻转位置
                max_index = pos
            if max_index == step:  # 当前最大位置等于当前步数时，前缀一致
                count += 1
        return count
