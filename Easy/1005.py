class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 首先对数组进行排序，便于处理负数
        nums.sort()
        n = len(nums)
        
        # 遍历数组，优先将负数变为正数
        for i in range(n):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        # 如果还有剩余操作次数且为奇数
        if k % 2 == 1:
            # 找到当前数组中的最小值进行取反
            min_val = min(nums)
            total_sum = sum(nums) - 2 * min_val
        else:
            total_sum = sum(nums)
        
        return total_sum
