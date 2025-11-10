class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 如果数组长度小于等于1，直接返回0
        if len(nums) <= 1:
            return 0
            
        operations = 0
        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            # 如果当前元素不大于前一个元素
            if nums[i] <= nums[i-1]:
                # 计算需要增加的次数，使当前元素比前一个元素大1
                diff = nums[i-1] - nums[i] + 1
                operations += diff
                # 更新当前元素的值
                nums[i] += diff
                
        return operations
