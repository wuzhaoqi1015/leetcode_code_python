class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右向左找到第一个降序的位置
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 从右向左找到第一个大于nums[i]的数
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换这两个数
            nums[i], nums[j] = nums[j], nums[i]
        
        # 反转i+1到末尾的部分
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
