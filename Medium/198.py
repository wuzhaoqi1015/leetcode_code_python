class Solution:
    def rob(self, nums: List[int]) -> int:
        # 处理特殊情况：空数组和单元素数组
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # 初始化动态规划数组
        n = len(nums)
        dp = [0] * n
        
        # 设置前两个房屋的基础情况
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # 从第三个房屋开始动态规划
        for i in range(2, n):
            # 当前房屋的最大金额 = max(偷当前房屋+前前个房屋的最大金额, 不偷当前房屋即前个房屋的最大金额)
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        # 返回最后一个房屋的最大金额
        return dp[n-1]
