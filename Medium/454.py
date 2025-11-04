class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 使用字典存储前两个数组的和及其出现次数
        sum_dict = {}
        for num1 in nums1:
            for num2 in nums2:
                total = num1 + num2
                sum_dict[total] = sum_dict.get(total, 0) + 1
        
        # 统计后两个数组的和与字典中对应负数的匹配次数
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                target = - (num3 + num4)
                if target in sum_dict:
                    count += sum_dict[target]
        
        return count
