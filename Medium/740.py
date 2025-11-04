class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 统计每个数字出现的次数并计算总点数
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num
        
        # 动态规划求解最大点数
        if max_num == 1:
            return points[1]
        
        # 初始化前两个状态
        dp = [0] * (max_num + 1)
        dp[1] = points[1]
        
        # 状态转移：对于每个数字，可以选择删除或不删除
        # 如果删除当前数字，则不能删除前一个数字
        # 如果不删除当前数字，则可以继承前一个数字的最大值
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return dp[max_num]
