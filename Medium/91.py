class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i]表示前i个字符的解码方法数
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串有一种解码方式
        
        for i in range(1, n + 1):
            # 检查单个字符解码
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # 检查两个字符解码
            if i >= 2:
                two_digit = int(s[i-2:i])
                if 10 <= two_digit <= 26:
                    dp[i] += dp[i-2]
        
        return dp[n]
