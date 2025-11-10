class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # 如果两个字符串相等，则没有特殊序列
        if a == b:
            return -1
        # 如果两个字符串不相等，则较长的字符串本身就是最长特殊序列
        # 因为它不可能是较短字符串的子序列（长度更长）
        return max(len(a), len(b))
