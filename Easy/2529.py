class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 使用二分查找找到第一个非负数的位置
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        neg_count = left  # 负数个数等于第一个非负数的索引
        
        # 使用二分查找找到第一个正数的位置
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        pos_count = len(nums) - left  # 正数个数等于总长度减去第一个正数的索引
        
        return max(neg_count, pos_count)
