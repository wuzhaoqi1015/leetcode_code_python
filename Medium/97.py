class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 如果s3长度不等于s1和s2长度之和，直接返回False
        if len(s1) + len(s2) != len(s3):
            return False
        
        # 使用动态规划，dp[i][j]表示s1的前i个字符和s2的前j个字符能否交错组成s3的前i+j个字符
        # 为了优化空间复杂度，使用一维数组
        n, m = len(s1), len(s2)
        dp = [False] * (m + 1)
        
        # 初始化：空字符串可以交错组成空字符串
        dp[0] = True
        
        # 初始化第一行：只使用s2的情况
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        
        # 动态规划过程
        for i in range(1, n + 1):
            # 更新当前行的第一个元素：只使用s1的情况
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                # 当前字符可能来自s1或s2
                # 如果来自s1：需要dp[j]为True且s1[i-1]等于s3[i+j-1]
                # 如果来自s2：需要dp[j-1]为True且s2[j-1]等于s3[i+j-1]
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[m]
