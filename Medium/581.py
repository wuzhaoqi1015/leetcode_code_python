class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # 从左到右找到第一个破坏递增的位置
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
            
        # 如果整个数组已经有序
        if left == n - 1:
            return 0
            
        # 从右到左找到第一个破坏递减的位置
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
            
        # 找到中间无序部分的最小值和最大值
        sub_min = min(nums[left:right + 1])
        sub_max = max(nums[left:right + 1])
        
        # 扩展左边界，确保左边所有元素都小于等于子数组最小值
        while left > 0 and nums[left - 1] > sub_min:
            left -= 1
            
        # 扩展右边界，确保右边所有元素都大于等于子数组最大值
        while right < n - 1 and nums[right + 1] < sub_max:
            right += 1
            
        return right - left + 1
