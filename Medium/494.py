class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 如果目标值绝对值大于总和，或者总和与目标值的差为奇数，则无解
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        # 计算正数和：设正数和为p，则负数和为total-p，有p - (total-p) = target => p = (total+target)//2
        pos_sum = (total + target) // 2
        
        # 使用动态规划，dp[j]表示和为j的方法数
        dp = [0] * (pos_sum + 1)
        dp[0] = 1  # 和为0的方法数为1（不选任何数）
        
        # 遍历每个数字
        for num in nums:
            # 从后往前更新，避免重复计算
            for j in range(pos_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[pos_sum]
