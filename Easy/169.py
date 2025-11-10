class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 使用Boyer-Moore投票算法
        candidate = None
        count = 0
        
        # 第一遍遍历：找到可能的候选元素
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # 由于题目保证存在多数元素，直接返回候选元素
        return candidate
