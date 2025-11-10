class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 使用集合存储所有非零元素，不同非零值的数量即为最少操作次数
        distinct_nums = set()
        for num in nums:
            if num != 0:
                distinct_nums.add(num)
        return len(distinct_nums)
