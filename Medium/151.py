class Solution:
    def reverseWords(self, s: str) -> str:
        # 去除首尾空格并将多个连续空格替换为单个空格
        s = s.strip()
        words = s.split()
        # 反转单词列表
        words.reverse()
        # 用单个空格连接单词
        return ' '.join(words)
