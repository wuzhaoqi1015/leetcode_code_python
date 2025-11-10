class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # 使用集合存储已经出现过的长度为2的子数组和
        seen = set()
        # 遍历数组，计算每个长度为2的子数组的和
        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            # 如果当前和在集合中已经存在，则返回True
            if current_sum in seen:
                return True
            # 否则将当前和加入集合
            seen.add(current_sum)
        # 遍历结束未找到重复和，返回False
        return False
