class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # dp[i][j]表示s1前i个字符和s2前j个字符的最小删除ASCII和
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化边界条件
        # 当s2为空时，需要删除s1的所有字符
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        # 当s1为空时，需要删除s2的所有字符
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        # 填充dp表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    # 字符相同，不需要删除
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 字符不同，选择删除s1当前字符或s2当前字符的最小代价
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), 
                                  dp[i][j-1] + ord(s2[j-1]))
        
        return dp[m][n]
