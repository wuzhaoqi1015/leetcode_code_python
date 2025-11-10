class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 遍历数组，将出现的数字对应的位置标记为负数
        for num in nums:
            index = abs(num) - 1  # 获取数字对应的索引位置
            if nums[index] > 0:   # 如果该位置数字为正数，则标记为负数
                nums[index] = -nums[index]
        
        result = []
        # 再次遍历数组，找出仍为正数的位置，这些位置对应的数字就是缺失的数字
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  # 位置索引+1即为缺失的数字
        
        return result
