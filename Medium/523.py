class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 使用哈希表记录前缀和模k第一次出现的索引
        remainder_map = {0: -1}  # 处理前缀和本身就是k的倍数的情况
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            
            # 如果相同的余数之前出现过，且子数组长度至少为2
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # 只记录第一次出现的索引
                remainder_map[remainder] = i
        
        return False
