class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 检查两个字符串是否可以通过某个基础字符串重复构成
        if str1 + str2 != str2 + str1:
            return ""
        
        # 计算两个字符串长度的最大公约数
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # 最大公约数长度对应的子串即为答案
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
