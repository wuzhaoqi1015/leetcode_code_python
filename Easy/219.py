class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 使用字典存储每个数字最近出现的索引
        num_dict = {}
        for i, num in enumerate(nums):
            # 如果数字已经在字典中，检查索引差是否小于等于k
            if num in num_dict and i - num_dict[num] <= k:
                return True
            # 更新数字的最新索引
            num_dict[num] = i
        return False
