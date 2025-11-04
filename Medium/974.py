class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 使用哈希表记录前缀和模k的余数出现的次数
        prefix_count = {0: 1}  # 初始化，前缀和为0的情况出现1次
        current_sum = 0
        result = 0
        
        for num in nums:
            # 计算当前前缀和
            current_sum += num
            # 计算当前前缀和模k的余数，处理负数情况
            remainder = current_sum % k
            # 如果余数为负数，转换为正数
            if remainder < 0:
                remainder += k
            
            # 如果该余数之前出现过，说明存在子数组和为k的倍数
            if remainder in prefix_count:
                result += prefix_count[remainder]
                prefix_count[remainder] += 1
            else:
                prefix_count[remainder] = 1
        
        return result
