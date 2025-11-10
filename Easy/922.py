class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 使用双指针方法，一个指针遍历偶数位置，一个指针遍历奇数位置
        n = len(nums)
        i, j = 0, 1  # i指向偶数位置，j指向奇数位置
        
        while i < n and j < n:
            # 找到偶数位置上不是偶数的位置
            while i < n and nums[i] % 2 == 0:
                i += 2
            # 找到奇数位置上不是奇数的位置
            while j < n and nums[j] % 2 == 1:
                j += 2
            # 如果都找到了需要交换的位置，则交换
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        
        return nums
