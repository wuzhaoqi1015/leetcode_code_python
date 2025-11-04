class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # dp[i]表示前i个元素分割后的最大和
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_max = 0
            # 尝试所有可能的分割点，j表示当前子数组的长度
            for j in range(1, min(k, i) + 1):
                # 更新当前子数组的最大值
                current_max = max(current_max, arr[i - j])
                # 状态转移：dp[i] = max(dp[i], dp[i-j] + current_max * j)
                dp[i] = max(dp[i], dp[i - j] + current_max * j)
        
        return dp[n]
