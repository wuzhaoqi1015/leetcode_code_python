class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 创建二维dp数组，dp[i][j]表示s[i:j+1]的最长回文子序列长度
        dp = [[0] * n for _ in range(n)]
        
        # 初始化对角线，单个字符的回文子序列长度为1
        for i in range(n):
            dp[i][i] = 1
            
        # 从右下角开始填充dp表，按列从后往前，按行从前往后
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    # 首尾字符相同，长度加2
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # 首尾字符不同，取去掉首或尾字符后的最大值
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        # 返回整个字符串的最长回文子序列长度
        return dp[0][n-1]
