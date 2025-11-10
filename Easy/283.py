class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用双指针，left指向当前非零元素应该放置的位置
        left = 0
        
        # 遍历数组，将非零元素移动到数组前面
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        
        # 将剩余位置填充为0
        for i in range(left, len(nums)):
            nums[i] = 0
