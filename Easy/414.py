class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 使用三个变量分别存储最大值、次大值和第三大值
        first = second = third = float('-inf')
        
        # 遍历数组中的每个数字
        for num in nums:
            # 如果数字等于当前最大值、次大值或第三大值，跳过重复值
            if num == first or num == second or num == third:
                continue
                
            # 如果数字大于当前最大值，更新三个值
            if num > first:
                third = second
                second = first
                first = num
            # 如果数字大于当前次大值，更新次大值和第三大值
            elif num > second:
                third = second
                second = num
            # 如果数字大于当前第三大值，更新第三大值
            elif num > third:
                third = num
        
        # 如果第三大值仍然是初始值，说明不存在第三大的数，返回最大值
        if third == float('-inf'):
            return first
        else:
            return third
