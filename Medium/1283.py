class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 计算给定除数下的总和
        def get_sum(divisor):
            total = 0
            for num in nums:
                # 向上取整
                total += (num + divisor - 1) // divisor
            return total
        
        # 二分查找范围：最小为1，最大为数组中的最大值
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            # 如果当前除数的总和小于等于阈值，说明除数可能可以更小
            if get_sum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
                
        return left
