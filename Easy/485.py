class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # 记录最大连续1的个数
        current_count = 0  # 记录当前连续1的个数
        
        for num in nums:
            if num == 1:
                current_count += 1  # 遇到1，当前计数加1
                max_count = max(max_count, current_count)  # 更新最大值
            else:
                current_count = 0  # 遇到0，重置当前计数
        
        return max_count
