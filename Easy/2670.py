class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = [0] * n
        
        # 计算每个位置的前缀不同元素数目
        prefix_set = set()
        prefix_count = [0] * n
        for i in range(n):
            prefix_set.add(nums[i])
            prefix_count[i] = len(prefix_set)
        
        # 计算每个位置的后缀不同元素数目
        suffix_set = set()
        suffix_count = [0] * n
        for i in range(n-1, -1, -1):
            suffix_count[i] = len(suffix_set)
            suffix_set.add(nums[i])
        
        # 计算差值数组
        for i in range(n):
            diff[i] = prefix_count[i] - suffix_count[i]
        
        return diff
