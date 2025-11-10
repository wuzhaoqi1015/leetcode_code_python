class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ""
        
        # 检查字符串是否美好
        def is_nice(sub):
            chars = set(sub)
            for char in chars:
                if char.islower():
                    if char.upper() not in chars:
                        return False
                else:
                    if char.lower() not in chars:
                        return False
            return True
        
        result = ""
        # 枚举所有可能的子串
        for i in range(n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if is_nice(substr) and len(substr) > len(result):
                    result = substr
                # 长度相同但出现更早的情况，由于我们按顺序枚举，第一个遇到的长度相同的自然就是最早的
                elif is_nice(substr) and len(substr) == len(result) and result == "":
                    result = substr
        
        return result
