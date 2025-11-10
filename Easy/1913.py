class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 对数组进行排序，以便找到最大和最小的元素
        nums.sort()
        n = len(nums)
        # 最大的两个数相乘得到最大乘积
        max_product = nums[n-1] * nums[n-2]
        # 最小的两个数相乘得到最小乘积
        min_product = nums[0] * nums[1]
        # 返回最大乘积与最小乘积的差值
        return max_product - min_product
