class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化最大乘积、最小乘积和结果变量
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        # 遍历数组，从第二个元素开始
        for i in range(1, len(nums)):
            # 保存当前的最大乘积值，用于计算最小乘积
            temp_max = max_prod
            
            # 更新最大乘积：考虑当前元素本身、当前元素与之前最大乘积的乘积、当前元素与之前最小乘积的乘积
            max_prod = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            
            # 更新最小乘积：考虑当前元素本身、当前元素与之前最大乘积的乘积、当前元素与之前最小乘积的乘积
            min_prod = min(nums[i], temp_max * nums[i], min_prod * nums[i])
            
            # 更新全局最大乘积结果
            result = max(result, max_prod)
        
        return result
