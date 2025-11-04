class Solution:
    def rob(self, nums: List[int]) -> int:
        # 处理特殊情况：如果只有一个房屋，直接返回该房屋的金额
        if len(nums) == 1:
            return nums[0]
        
        # 定义辅助函数，用于计算在直线排列房屋中的最大偷窃金额
        def linear_rob(arr):
            # 初始化动态规划数组
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            
            # 创建dp数组，dp[i]表示偷窃到第i个房屋时的最大金额
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            # 填充dp数组
            for i in range(2, n):
                # 对于每个房屋，选择偷或不偷
                # 偷：当前房屋金额 + 前两个房屋的最大金额
                # 不偷：前一个房屋的最大金额
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            
            return dp[n-1]
        
        # 由于房屋围成圈，第一个和最后一个不能同时偷
        # 情况1：不偷第一个房屋，偷窃范围从第二个到最后一个
        # 情况2：不偷最后一个房屋，偷窃范围从第一个到倒数第二个
        # 取两种情况的最大值
        return max(linear_rob(nums[1:]), linear_rob(nums[:-1]))
