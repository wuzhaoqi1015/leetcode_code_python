class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # 找到数组中的最大值和最小值
        max_val = max(nums)
        min_val = min(nums)
        
        # 计算原始分数
        original_score = max_val - min_val
        
        # 如果原始分数小于等于2k，则可以通过调整使分数为0
        # 否则最小分数为原始分数减去2k
        if original_score <= 2 * k:
            return 0
        else:
            return original_score - 2 * k
