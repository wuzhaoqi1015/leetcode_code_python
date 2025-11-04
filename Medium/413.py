class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        total_count = 0
        current_count = 0
        
        # 遍历数组，检查每个可能的等差数列
        for i in range(2, n):
            # 如果当前元素与前两个元素构成等差数列
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current_count += 1
                total_count += current_count
            else:
                current_count = 0
        
        return total_count
