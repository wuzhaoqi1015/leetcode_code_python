class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 确保mid指向每对元素的第一个
            if mid % 2 == 1:
                mid -= 1
            # 如果mid和mid+1相等，说明单个元素在右侧
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
