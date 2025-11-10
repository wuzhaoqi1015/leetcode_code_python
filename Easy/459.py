class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # 遍历可能的子串长度，从1到n//2
        for i in range(1, n // 2 + 1):
            # 如果当前长度不能整除总长度，跳过
            if n % i != 0:
                continue
            # 获取候选子串
            substr = s[:i]
            # 检查整个字符串是否由该子串重复构成
            if substr * (n // i) == s:
                return True
        return False
