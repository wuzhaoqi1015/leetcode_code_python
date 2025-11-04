class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        total_sum = sum(nums)  # 计算数组所有元素的和
        current_f = 0  # 计算初始F(0)的值
        
        # 计算初始旋转函数值F(0)
        for i in range(n):
            current_f += i * nums[i]
        
        max_f = current_f  # 初始化最大值为F(0)
        
        # 通过递推关系计算其他旋转函数值
        # F(k) = F(k-1) + total_sum - n * nums[n-k]
        for k in range(1, n):
            current_f = current_f + total_sum - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f
