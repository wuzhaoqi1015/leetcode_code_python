class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # 如果总和为奇数，不可能分割成两个和相等的子集
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # 初始化动态规划数组，dp[j]表示能否得到和为j的子集
        dp = [False] * (target + 1)
        dp[0] = True  # 和为0总是可以实现的（空集）
        
        # 遍历数组中的每个数字
        for num in nums:
            # 从后往前更新dp数组，避免重复使用同一个数字
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        
        return dp[target]
