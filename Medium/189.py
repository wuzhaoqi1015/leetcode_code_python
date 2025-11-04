class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 处理k大于数组长度的情况
        if k == 0:  # 如果k为0或n的倍数，无需旋转
            return
        
        # 三次反转法：空间复杂度O(1)
        # 第一步：反转整个数组
        self.reverse(nums, 0, n - 1)
        # 第二步：反转前k个元素
        self.reverse(nums, 0, k - 1)
        # 第三步：反转剩余元素
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        # 辅助函数：反转数组中指定范围的元素
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
