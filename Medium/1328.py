class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        # 如果字符串长度小于等于1，无法通过替换一个字符使其变成非回文
        if n <= 1:
            return ""
        # 将字符串转换为列表以便修改
        s_list = list(palindrome)
        # 遍历字符串的前半部分
        for i in range(n // 2):
            # 如果当前字符不是'a'，将其替换为'a'即可得到字典序最小的非回文串
            if s_list[i] != 'a':
                s_list[i] = 'a'
                return ''.join(s_list)
        # 如果前半部分都是'a'，将最后一个字符替换为'b'
        s_list[-1] = 'b'
        return ''.join(s_list)
