class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        
        # 计算元素和与数字和
        for num in nums:
            element_sum += num
            # 计算每个数字的数位和
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
        
        # 返回绝对差
        return abs(element_sum - digit_sum)
