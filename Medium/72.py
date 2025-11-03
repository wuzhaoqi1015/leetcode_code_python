class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 初始化dp数组，dp[i][j]表示word1前i个字符转换为word2前j个字符的最小操作数
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化边界条件
        for i in range(m + 1):
            dp[i][0] = i  # word1前i个字符转换为空字符串需要i次删除操作
        for j in range(n + 1):
            dp[0][j] = j  # 空字符串转换为word2前j个字符需要j次插入操作
            
        # 动态规划填充dp数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    # 字符相同，不需要操作
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 字符不同，取三种操作的最小值加1
                    # 删除：dp[i-1][j] + 1
                    # 插入：dp[i][j-1] + 1  
                    # 替换：dp[i-1][j-1] + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
        return dp[m][n]
