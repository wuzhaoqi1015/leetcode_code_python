class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][diff] 表示以 nums[i] 结尾，公差为 diff 的最长等差子序列长度
        dp = [dict() for _ in range(n)]
        max_len = 2  # 最小等差子序列长度为2
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # 如果 nums[j] 已经有公差为 diff 的序列，则在其基础上加1
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    # 否则从 nums[j] 开始，与 nums[i] 形成长度为2的序列
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        
        return max_len
