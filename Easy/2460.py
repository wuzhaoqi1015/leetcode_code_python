class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 执行n-1步操作
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # 将所有非零元素移动到前面，零元素移动到末尾
        result = []
        zero_count = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1
        
        # 在末尾添加零
        result.extend([0] * zero_count)
        return result
