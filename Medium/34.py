class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 处理空数组情况
        if not nums:
            return [-1, -1]
        
        # 二分查找左边界
        left, right = 0, len(nums) - 1
        left_bound = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_bound = mid
                right = mid - 1  # 继续在左半部分查找
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 如果左边界没找到，说明目标值不存在
        if left_bound == -1:
            return [-1, -1]
        
        # 二分查找右边界
        left, right = 0, len(nums) - 1
        right_bound = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right_bound = mid
                left = mid + 1  # 继续在右半部分查找
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [left_bound, right_bound]
