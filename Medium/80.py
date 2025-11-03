class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果数组长度小于等于2，直接返回原长度
        if len(nums) <= 2:
            return len(nums)
        
        # 使用双指针法，slow指针指向当前有效数组的末尾
        slow = 2
        # fast指针用于遍历整个数组
        for fast in range(2, len(nums)):
            # 如果当前元素不等于slow-2位置的元素，说明可以保留
            # 因为数组有序，这样能确保相同元素最多出现两次
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        
        # 返回新数组的长度
        return slow
