class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        # 遍历所有长度为3的子串
        for i in range(n - 2):
            # 检查当前子串的三个字符是否互不相同
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                count += 1
        return count
