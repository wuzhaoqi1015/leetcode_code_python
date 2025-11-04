class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # 使用字典记录以每个字符结尾的最长连续子串长度
        dp = {}
        length = 0
        for i in range(len(s)):
            # 检查当前字符是否与前一个字符在base中连续
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i] == 'a')):
                length += 1
            else:
                length = 1
            # 更新以当前字符结尾的最长连续子串长度
            dp[s[i]] = max(dp.get(s[i], 0), length)
        
        # 返回所有字符对应最长长度的总和
        return sum(dp.values())
