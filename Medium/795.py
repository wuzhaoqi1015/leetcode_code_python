class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # 定义辅助函数计算所有元素都不超过bound的子数组数量
        def count_subarrays(bound):
            count = 0
            current = 0
            for num in nums:
                # 如果当前元素不超过bound，可以扩展子数组
                if num <= bound:
                    current += 1
                else:
                    current = 0
                # 累加以当前元素结尾的满足条件的子数组数量
                count += current
            return count
        
        # 总子数组数量 = 所有元素不超过right的子数组数量 - 所有元素不超过left-1的子数组数量
        return count_subarrays(right) - count_subarrays(left - 1)
