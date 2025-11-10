class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # 使用集合存储所有数字，便于快速查找
        num_set = set(nums)
        max_k = -1
        
        # 遍历数组中的每个数字
        for num in nums:
            # 只考虑正数，并且检查其负数是否存在于集合中
            if num > 0 and -num in num_set:
                # 更新最大正整数
                if num > max_k:
                    max_k = num
        
        return max_k
