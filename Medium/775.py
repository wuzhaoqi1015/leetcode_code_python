class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # 局部倒置一定是全局倒置，所以全局倒置数量 >= 局部倒置数量
        # 要使两者相等，必须确保所有全局倒置都是局部倒置
        # 即对于任意 i < j 且 j > i+1，不能有 nums[i] > nums[j]
        # 等价于每个元素 nums[i] 只能出现在位置 i-1, i, i+1 上
        n = len(nums)
        for i in range(n):
            # 检查当前元素与目标位置的差值是否超过1
            if abs(nums[i] - i) > 1:
                return False
        return True
