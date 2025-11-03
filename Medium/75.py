class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用三指针法进行一趟扫描
        left = 0  # 指向0的右边界
        right = len(nums) - 1  # 指向2的左边界
        curr = 0  # 当前遍历指针
        
        while curr <= right:
            if nums[curr] == 0:
                # 将0交换到左边界
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                # 将2交换到右边界
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                # 注意这里curr不增加，因为交换过来的元素需要重新判断
            else:
                # 遇到1直接跳过
                curr += 1
