class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 初始化最远可达位置为0
        max_reach = 0
        # 遍历数组中的每个位置
        for i in range(len(nums)):
            # 如果当前位置已经超过了之前能到达的最远位置，说明无法到达当前位置
            if i > max_reach:
                return False
            # 更新能够到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            # 如果最远位置已经能够到达或超过最后一个位置，提前返回True
            if max_reach >= len(nums) - 1:
                return True
        # 遍历完成后检查是否到达最后一个位置
        return max_reach >= len(nums) - 1
