class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 如果数组没有旋转或者只有一个元素，直接返回第一个元素
        if nums[right] >= nums[0]:
            return nums[0]
        
        # 二分查找旋转点
        while left <= right:
            mid = (left + right) // 2
            # 如果中间元素大于后一个元素，说明找到了旋转点
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # 如果中间元素小于前一个元素，说明中间元素就是最小值
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # 如果中间元素大于第一个元素，说明旋转点在右侧
            if nums[mid] > nums[0]:
                left = mid + 1
            # 否则旋转点在左侧
            else:
                right = mid - 1
        return -1
