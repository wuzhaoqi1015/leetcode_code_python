class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 使用二分查找实现O(log n)时间复杂度
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 如果中间元素大于右侧元素，说明峰值在左侧或中间
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 否则峰值在右侧
            else:
                left = mid + 1
        
        # 当left == right时，找到峰值元素
        return left
