class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 初始化余数为0,1,2时的最大和
        dp = [0, -10**9, -10**9]
        
        for num in nums:
            # 创建当前dp的副本用于更新
            current_dp = dp[:]
            for remainder in range(3):
                # 计算新的余数位置
                new_remainder = (remainder + num) % 3
                # 更新新余数位置的最大值
                dp[new_remainder] = max(dp[new_remainder], current_dp[remainder] + num)
        
        # 返回余数为0的最大和，如果没有则为0
        return dp[0] if dp[0] >= 0 else 0
