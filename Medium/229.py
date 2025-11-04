class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 使用摩尔投票法，最多有两个候选元素
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # 第一遍遍历，找出可能的候选元素
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 第二遍遍历，统计候选元素的真实出现次数
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        n = len(nums)
        threshold = n // 3
        
        # 检查候选元素是否满足条件
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
        
        return result
