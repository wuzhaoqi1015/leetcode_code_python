class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 处理空数组的情况
        if not nums:
            return 0
            
        # 使用双指针法，slow指向当前唯一元素的最后一个位置
        slow = 0
        
        # fast指针遍历整个数组
        for fast in range(1, len(nums)):
            # 当遇到不同元素时，将slow指针后移并更新元素
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        # 返回唯一元素的个数，slow是索引，需要+1
        return slow + 1
