class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1  # 记录最大得分
        result = float('inf')  # 记录结果，初始化为最大值
        
        for d in divisors:
            count = 0  # 当前除数的得分
            for num in nums:
                if num % d == 0:  # 如果num能被d整除
                    count += 1
            
            # 如果当前得分大于最大得分，或者得分相同但除数更小
            if count > max_score or (count == max_score and d < result):
                max_score = count
                result = d
        
        return result
