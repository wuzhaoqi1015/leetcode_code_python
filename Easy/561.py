class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 对数组进行排序，这样相邻的两个数可以组成一对
        nums.sort()
        total = 0
        # 遍历排序后的数组，取每对中的较小值（即偶数索引位置的元素）
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
