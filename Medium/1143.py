class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 获取两个字符串的长度
        m, n = len(text1), len(text2)
        # 创建动态规划表，大小为(m+1) x (n+1)，初始化为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 遍历两个字符串的所有字符
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前字符匹配
                if text1[i - 1] == text2[j - 1]:
                    # 取左上角值加1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 取左边和上边值的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 返回右下角的值，即最长公共子序列的长度
        return dp[m][n]
